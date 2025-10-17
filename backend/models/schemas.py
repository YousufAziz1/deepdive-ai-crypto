from pydantic import BaseModel, Field
from typing import Optional, List, Dict
from enum import Enum

class HealthResponse(BaseModel):
    status: str
    service: str
    version: str

class InputType(str, Enum):
    PROJECT_NAME = "project_name"
    CONTRACT_ADDRESS = "contract_address"
    TWITTER_HANDLE = "twitter_handle"

class AnalysisRequest(BaseModel):
    input: str = Field(..., description="Project name, contract address, or Twitter handle")
    input_type: Optional[InputType] = Field(None, description="Type of input provided")

class TokenMetrics(BaseModel):
    price: Optional[float] = None
    market_cap: Optional[float] = None
    fully_diluted_valuation: Optional[float] = None
    volume_24h: Optional[float] = None
    holders: Optional[int] = None
    price_change_24h: Optional[float] = None
    price_change_7d: Optional[float] = None

class Tokenomics(BaseModel):
    total_supply: Optional[float] = None
    circulating_supply: Optional[float] = None
    max_supply: Optional[float] = None
    distribution: Optional[Dict[str, float]] = None
    vesting_schedule: Optional[str] = None

class SocialMetrics(BaseModel):
    twitter_followers: Optional[int] = None
    twitter_engagement_rate: Optional[float] = None
    sentiment_score: Optional[float] = None
    recent_mentions: Optional[int] = None

class TechnicalMetrics(BaseModel):
    github_stars: Optional[int] = None
    github_forks: Optional[int] = None
    commits_last_month: Optional[int] = None
    contributors: Optional[int] = None
    last_commit_date: Optional[str] = None

class TeamInfo(BaseModel):
    members: List[Dict[str, str]] = []
    linkedin_profiles: List[str] = []
    past_projects: List[str] = []

class Scores(BaseModel):
    team_credibility: int = Field(0, ge=0, le=10)
    product_market_fit: int = Field(0, ge=0, le=10)
    tokenomics_health: int = Field(0, ge=0, le=10)
    community_strength: int = Field(0, ge=0, le=10)
    technical_development: int = Field(0, ge=0, le=10)
    total: int = Field(0, ge=0, le=50)

class RiskLevel(str, Enum):
    GREEN = "green"
    YELLOW = "yellow"
    RED = "red"

class RiskFlags(BaseModel):
    level: RiskLevel
    flags: List[str] = []

class InvestmentThesis(BaseModel):
    bull_case: List[str]
    bear_case: List[str]
    recommendation: str

class ProjectData(BaseModel):
    project_name: str
    symbol: Optional[str] = None
    contract_address: Optional[str] = None
    website: Optional[str] = None
    description: Optional[str] = None
    token_metrics: TokenMetrics
    tokenomics: Tokenomics
    social_metrics: SocialMetrics
    technical_metrics: TechnicalMetrics
    team_info: TeamInfo

class AnalysisResponse(BaseModel):
    project_data: ProjectData
    executive_summary: str
    scores: Scores
    risk_flags: RiskFlags
    investment_thesis: InvestmentThesis
    report_url: Optional[str] = None
    analysis_timestamp: str

class ComparisonRequest(BaseModel):
    projects: List[str] = Field(..., min_items=2, max_items=3)

class ComparisonResponse(BaseModel):
    projects: List[AnalysisResponse]
    comparative_summary: str
