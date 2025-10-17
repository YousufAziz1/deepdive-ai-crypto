import httpx
from typing import Dict, List
from config import settings
import logging
import json

logger = logging.getLogger(__name__)

class ROMAService:
    """OpenRouter AI Integration for AI Analysis"""
    BASE_URL = "https://openrouter.ai/api/v1"
    
    def __init__(self):
        self.api_key = settings.OPENROUTER_API_KEY
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "http://localhost:3000",
            "X-Title": "DeepDive AI"
        }
    
    async def generate_executive_summary(self, project_data: Dict) -> str:
        """Generate 100-word executive summary using ROMA"""
        try:
            prompt = f"""
Analyze this crypto project and provide a concise 100-word executive summary:

Project: {project_data.get('project_name')}
Description: {project_data.get('description', 'N/A')}
Price: ${project_data.get('token_metrics', {}).get('price', 'N/A')}
Market Cap: ${project_data.get('token_metrics', {}).get('market_cap', 'N/A')}
24h Volume: ${project_data.get('token_metrics', {}).get('volume_24h', 'N/A')}

Provide a professional, objective summary covering: what the project does, key metrics, and notable observations.
"""
            
            # Call OpenRouter API
            summary = await self._call_ai(prompt, max_tokens=150)
            return summary
        except Exception as e:
            logger.error(f"Error generating summary: {e}")
            return self._generate_fallback_summary(project_data)
    
    async def calculate_scores(self, project_data: Dict) -> Dict[str, int]:
        """Calculate 5-category scores using ROMA analysis"""
        try:
            prompt = f"""
Analyze this crypto project and provide scores (0-10) for these categories:
1. Team Credibility
2. Product-Market Fit
3. Tokenomics Health
4. Community Strength
5. Technical Development

Project Data:
- Name: {project_data.get('project_name')}
- GitHub Stars: {project_data.get('technical_metrics', {}).get('github_stars', 'N/A')}
- Contributors: {project_data.get('technical_metrics', {}).get('contributors', 'N/A')}
- Commits (Last Month): {project_data.get('technical_metrics', {}).get('commits_last_month', 'N/A')}
- Twitter Followers: {project_data.get('social_metrics', {}).get('twitter_followers', 'N/A')}
- Market Cap: ${project_data.get('token_metrics', {}).get('market_cap', 'N/A')}
- 24h Volume: ${project_data.get('token_metrics', {}).get('volume_24h', 'N/A')}

Respond in JSON format:
{{
  "team_credibility": <0-10>,
  "product_market_fit": <0-10>,
  "tokenomics_health": <0-10>,
  "community_strength": <0-10>,
  "technical_development": <0-10>
}}
"""
            
            response = await self._call_ai(prompt, max_tokens=200)
            scores = json.loads(response)
            scores["total"] = sum(scores.values())
            return scores
        except Exception as e:
            logger.error(f"Error calculating scores: {e}")
            return self._generate_fallback_scores(project_data)
    
    async def analyze_risk_flags(self, project_data: Dict) -> Dict:
        """Identify risk flags and assign risk level"""
        try:
            prompt = f"""
Analyze this crypto project for risk factors:

Project: {project_data.get('project_name')}
Market Cap: ${project_data.get('token_metrics', {}).get('market_cap', 'N/A')}
Volume 24h: ${project_data.get('token_metrics', {}).get('volume_24h', 'N/A')}
Holders: {project_data.get('token_metrics', {}).get('holders', 'N/A')}
Last GitHub Commit: {project_data.get('technical_metrics', {}).get('last_commit_date', 'N/A')}

Identify risk flags and assign overall risk level (green/yellow/red).

Respond in JSON format:
{{
  "level": "green|yellow|red",
  "flags": ["flag1", "flag2", ...]
}}
"""
            
            response = await self._call_ai(prompt, max_tokens=300)
            return json.loads(response)
        except Exception as e:
            logger.error(f"Error analyzing risks: {e}")
            return self._generate_fallback_risk_analysis(project_data)
    
    async def generate_investment_thesis(self, project_data: Dict, scores: Dict) -> Dict:
        """Generate bull case, bear case, and recommendation"""
        try:
            prompt = f"""
Create an investment thesis for this crypto project:

Project: {project_data.get('project_name')}
Total Score: {scores.get('total', 0)}/50
Market Cap: ${project_data.get('token_metrics', {}).get('market_cap', 'N/A')}
Community: {project_data.get('social_metrics', {}).get('twitter_followers', 'N/A')} followers

Provide:
1. Bull Case (3-4 key points)
2. Bear Case (3-4 key points)
3. Overall Recommendation (Strong Buy/Buy/Moderate Buy/Hold/Sell)

Respond in JSON format:
{{
  "bull_case": ["point1", "point2", ...],
  "bear_case": ["point1", "point2", ...],
  "recommendation": "recommendation"
}}
"""
            
            response = await self._call_ai(prompt, max_tokens=400)
            return json.loads(response)
        except Exception as e:
            logger.error(f"Error generating thesis: {e}")
            return self._generate_fallback_thesis(project_data, scores)
    
    async def _call_ai(self, prompt: str, max_tokens: int = 200) -> str:
        """Make API call to OpenRouter"""
        if not self.api_key:
            raise Exception("OpenRouter API key not configured")
        
        try:
            async with httpx.AsyncClient(timeout=30.0) as client:
                response = await client.post(
                    f"{self.BASE_URL}/chat/completions",
                    headers=self.headers,
                    json={
                        "model": "openai/gpt-3.5-turbo",
                        "messages": [
                            {"role": "system", "content": "You are a crypto analyst AI that provides concise, objective analysis."},
                            {"role": "user", "content": prompt}
                        ],
                        "max_tokens": max_tokens,
                        "temperature": 0.7
                    }
                )
                response.raise_for_status()
                data = response.json()
                return data.get("choices", [{}])[0].get("message", {}).get("content", "").strip()
        except Exception as e:
            logger.error(f"OpenRouter API call failed: {e}")
            raise
    
    # Fallback methods when ROMA API is unavailable
    def _generate_fallback_summary(self, project_data: Dict) -> str:
        """Generate basic summary without AI"""
        name = project_data.get('project_name', 'Unknown')
        price = project_data.get('token_metrics', {}).get('price')
        mcap = project_data.get('token_metrics', {}).get('market_cap')
        
        return f"{name} is a cryptocurrency project with a current price of ${price:.4f if price else 0} and market cap of ${mcap:,.0f if mcap else 0}. The project shows activity in development and community engagement. Further analysis is recommended for investment decisions."
    
    def _generate_fallback_scores(self, project_data: Dict) -> Dict[str, int]:
        """Generate basic scores based on available metrics"""
        metrics = {
            "team_credibility": 5,
            "product_market_fit": 5,
            "tokenomics_health": 5,
            "community_strength": 5,
            "technical_development": 5
        }
        
        # Adjust based on available data
        if project_data.get('technical_metrics', {}).get('github_stars', 0) > 1000:
            metrics["technical_development"] += 2
        if project_data.get('social_metrics', {}).get('twitter_followers', 0) > 10000:
            metrics["community_strength"] += 2
        
        metrics["total"] = sum(v for k, v in metrics.items() if k != "total")
        return metrics
    
    def _generate_fallback_risk_analysis(self, project_data: Dict) -> Dict:
        """Generate basic risk analysis"""
        flags = []
        level = "yellow"
        
        if not project_data.get('technical_metrics', {}).get('github_stars'):
            flags.append("No public GitHub repository found")
        
        if project_data.get('token_metrics', {}).get('volume_24h', 0) < 100000:
            flags.append("Low trading volume")
        
        if len(flags) == 0:
            level = "green"
        elif len(flags) > 2:
            level = "red"
        
        return {"level": level, "flags": flags}
    
    def _generate_fallback_thesis(self, project_data: Dict, scores: Dict) -> Dict:
        """Generate basic investment thesis"""
        total_score = scores.get('total', 25)
        
        if total_score >= 40:
            recommendation = "Strong Buy"
        elif total_score >= 35:
            recommendation = "Buy"
        elif total_score >= 25:
            recommendation = "Moderate Buy"
        elif total_score >= 20:
            recommendation = "Hold"
        else:
            recommendation = "Avoid"
        
        return {
            "bull_case": [
                "Active development community",
                "Growing market presence",
                "Strong fundamentals"
            ],
            "bear_case": [
                "Market volatility",
                "Competition in the space",
                "Regulatory uncertainty"
            ],
            "recommendation": recommendation
        }
