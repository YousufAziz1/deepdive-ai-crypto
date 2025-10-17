from typing import Dict, Optional
from datetime import datetime
import logging

from services.coingecko_service import CoinGeckoService
from services.defillama_service import DefiLlamaService
from services.github_service import GitHubService
from services.twitter_service import TwitterService
from services.roma_service import ROMAService
from models.schemas import (
    ProjectData, TokenMetrics, Tokenomics, SocialMetrics,
    TechnicalMetrics, TeamInfo, AnalysisResponse, Scores,
    RiskFlags, InvestmentThesis
)

logger = logging.getLogger(__name__)

class AggregationService:
    """Main service to aggregate data from all sources and perform AI analysis"""
    
    def __init__(self):
        self.coingecko = CoinGeckoService()
        self.defillama = DefiLlamaService()
        self.github = GitHubService()
        self.twitter = TwitterService()
        self.roma = ROMAService()
    
    async def analyze_project(self, project_input: str, input_type: Optional[str] = None) -> AnalysisResponse:
        """
        Main analysis pipeline
        1. Detect input type if not provided
        2. Aggregate data from all sources
        3. Run AI analysis using ROMA
        4. Return comprehensive analysis
        """
        logger.info(f"Starting analysis for: {project_input}")
        
        # Step 1: Detect input type
        if not input_type:
            input_type = self._detect_input_type(project_input)
        
        # Step 2: Aggregate all data
        project_data = await self._aggregate_project_data(project_input, input_type)
        
        # Step 3: AI Analysis using ROMA
        executive_summary = await self.roma.generate_executive_summary(project_data.dict())
        scores_dict = await self.roma.calculate_scores(project_data.dict())
        risk_data = await self.roma.analyze_risk_flags(project_data.dict())
        thesis_data = await self.roma.generate_investment_thesis(project_data.dict(), scores_dict)
        
        # Build response
        scores = Scores(**scores_dict)
        risk_flags = RiskFlags(**risk_data)
        investment_thesis = InvestmentThesis(**thesis_data)
        
        return AnalysisResponse(
            project_data=project_data,
            executive_summary=executive_summary,
            scores=scores,
            risk_flags=risk_flags,
            investment_thesis=investment_thesis,
            analysis_timestamp=datetime.utcnow().isoformat()
        )
    
    def _detect_input_type(self, input_str: str) -> str:
        """Auto-detect input type"""
        input_str = input_str.strip()
        
        # Check if it's a contract address (0x... with 40 hex chars)
        if input_str.startswith("0x") and len(input_str) == 42:
            return "contract_address"
        
        # Check if it's a Twitter handle (@...)
        if input_str.startswith("@"):
            return "twitter_handle"
        
        # Default to project name
        return "project_name"
    
    async def _aggregate_project_data(self, project_input: str, input_type: str) -> ProjectData:
        """Aggregate data from all sources"""
        
        # Initialize with default values
        project_name = project_input
        contract_address = None
        twitter_handle = None
        
        # Resolve based on input type
        if input_type == "twitter_handle":
            twitter_handle = project_input
            # Try to find project name from Twitter bio
            user_data = await self.twitter.get_user_by_username(twitter_handle)
            if user_data:
                # Extract project name from username or description
                project_name = user_data.username
        
        elif input_type == "contract_address":
            contract_address = project_input
            # Try to find project name from CoinGecko
            # This is simplified - in production, use blockchain explorer
            project_name = "Unknown Project"
        
        # Fetch data from all sources in parallel
        logger.info(f"Fetching data for project: {project_name}")
        
        # CoinGecko data
        token_metrics_data = await self.coingecko.get_token_metrics(project_name)
        tokenomics_data = await self.coingecko.get_tokenomics(project_name)
        
        # DefiLlama data
        tvl_data = await self.defillama.get_tvl_data(project_name)
        
        # GitHub data
        technical_data = await self.github.get_technical_metrics(project_name)
        
        # Twitter data
        social_data = await self.twitter.get_social_metrics(project_name, twitter_handle)
        sentiment = await self.twitter.get_sentiment_score(project_name)
        social_data["sentiment_score"] = sentiment
        
        # Build structured data
        token_metrics = TokenMetrics(**token_metrics_data)
        tokenomics = Tokenomics(**tokenomics_data)
        social_metrics = SocialMetrics(**social_data)
        technical_metrics = TechnicalMetrics(**technical_data)
        team_info = TeamInfo()  # Would need LinkedIn API or manual data
        
        # Get additional info from CoinGecko
        coin_id = await self.coingecko.search_coin(project_name)
        coin_data = await self.coingecko.get_coin_data(coin_id) if coin_id else None
        
        website = None
        description = None
        symbol = None
        
        if coin_data:
            website = coin_data.get("links", {}).get("homepage", [None])[0]
            description = coin_data.get("description", {}).get("en", "")
            symbol = coin_data.get("symbol", "").upper()
            if not contract_address:
                contract_address = await self.coingecko.get_contract_address(coin_id)
        
        return ProjectData(
            project_name=project_name,
            symbol=symbol,
            contract_address=contract_address,
            website=website,
            description=description,
            token_metrics=token_metrics,
            tokenomics=tokenomics,
            social_metrics=social_metrics,
            technical_metrics=technical_metrics,
            team_info=team_info
        )
    
    async def compare_projects(self, project_names: list) -> Dict:
        """Compare multiple projects side-by-side"""
        analyses = []
        
        for project_name in project_names:
            try:
                analysis = await self.analyze_project(project_name)
                analyses.append(analysis)
            except Exception as e:
                logger.error(f"Error analyzing {project_name}: {e}")
        
        # Generate comparative summary using ROMA
        comparison_prompt = f"Compare these {len(analyses)} crypto projects and provide key differences:"
        for analysis in analyses:
            comparison_prompt += f"\n- {analysis.project_data.project_name}: Score {analysis.scores.total}/50"
        
        try:
            comparative_summary = await self.roma._call_ai(comparison_prompt, max_tokens=300)
        except:
            comparative_summary = "Comparison of selected projects based on aggregated metrics."
        
        return {
            "projects": analyses,
            "comparative_summary": comparative_summary
        }
