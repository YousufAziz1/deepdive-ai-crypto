from fastapi import APIRouter, HTTPException
from typing import List, Dict
import json
import os
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

# In-memory storage for demo (in production, use a database)
SHOWCASE_FILE = "showcase_projects.json"

@router.get("/showcase")
async def get_showcase_projects() -> List[Dict]:
    """
    Get list of pre-analyzed showcase projects
    
    Returns 20+ projects with cached analysis results
    """
    try:
        if os.path.exists(SHOWCASE_FILE):
            with open(SHOWCASE_FILE, 'r') as f:
                return json.load(f)
        else:
            # Return sample data if file doesn't exist
            return get_sample_showcase_projects()
    except Exception as e:
        logger.error(f"Error loading showcase projects: {e}")
        return get_sample_showcase_projects()

@router.post("/showcase")
async def add_showcase_project(project_data: Dict) -> Dict:
    """
    Add a project to the showcase
    
    Used to build the library of pre-analyzed projects
    """
    try:
        projects = []
        if os.path.exists(SHOWCASE_FILE):
            with open(SHOWCASE_FILE, 'r') as f:
                projects = json.load(f)
        
        projects.append(project_data)
        
        with open(SHOWCASE_FILE, 'w') as f:
            json.dump(projects, f, indent=2)
        
        return {"status": "success", "message": "Project added to showcase"}
    except Exception as e:
        logger.error(f"Error adding showcase project: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/watchlist")
async def get_watchlist() -> List[Dict]:
    """
    Get user's watchlist projects
    
    Returns projects marked for daily monitoring
    """
    # Placeholder - in production, this would be user-specific
    return []

@router.post("/watchlist")
async def add_to_watchlist(project_name: str) -> Dict:
    """
    Add a project to watchlist
    
    Enables daily monitoring and alerts
    """
    # Placeholder implementation
    return {
        "status": "success",
        "message": f"{project_name} added to watchlist"
    }

def get_sample_showcase_projects() -> List[Dict]:
    """Return sample showcase projects"""
    return [
        {
            "name": "Ethereum",
            "symbol": "ETH",
            "score": 48,
            "risk": "green",
            "category": "Layer 1"
        },
        {
            "name": "Render",
            "symbol": "RNDR",
            "score": 42,
            "risk": "green",
            "category": "Infrastructure"
        },
        {
            "name": "Chainlink",
            "symbol": "LINK",
            "score": 45,
            "risk": "green",
            "category": "Oracle"
        },
        {
            "name": "Uniswap",
            "symbol": "UNI",
            "score": 43,
            "risk": "green",
            "category": "DEX"
        },
        {
            "name": "Aave",
            "symbol": "AAVE",
            "score": 44,
            "risk": "green",
            "category": "Lending"
        },
        {
            "name": "Polygon",
            "symbol": "MATIC",
            "score": 41,
            "risk": "yellow",
            "category": "Layer 2"
        },
        {
            "name": "Arbitrum",
            "symbol": "ARB",
            "score": 40,
            "risk": "yellow",
            "category": "Layer 2"
        },
        {
            "name": "Optimism",
            "symbol": "OP",
            "score": 39,
            "risk": "yellow",
            "category": "Layer 2"
        },
        {
            "name": "Solana",
            "symbol": "SOL",
            "score": 38,
            "risk": "yellow",
            "category": "Layer 1"
        },
        {
            "name": "Avalanche",
            "symbol": "AVAX",
            "score": 37,
            "risk": "yellow",
            "category": "Layer 1"
        },
        {
            "name": "The Graph",
            "symbol": "GRT",
            "score": 36,
            "risk": "yellow",
            "category": "Infrastructure"
        },
        {
            "name": "Lido",
            "symbol": "LDO",
            "score": 42,
            "risk": "green",
            "category": "Staking"
        },
        {
            "name": "Maker",
            "symbol": "MKR",
            "score": 43,
            "risk": "green",
            "category": "Stablecoin"
        },
        {
            "name": "Curve",
            "symbol": "CRV",
            "score": 40,
            "risk": "yellow",
            "category": "DEX"
        },
        {
            "name": "Synthetix",
            "symbol": "SNX",
            "score": 38,
            "risk": "yellow",
            "category": "Derivatives"
        },
        {
            "name": "Injective",
            "symbol": "INJ",
            "score": 37,
            "risk": "yellow",
            "category": "Layer 1"
        },
        {
            "name": "Celestia",
            "symbol": "TIA",
            "score": 36,
            "risk": "yellow",
            "category": "Modular Chain"
        },
        {
            "name": "Pendle",
            "symbol": "PENDLE",
            "score": 35,
            "risk": "yellow",
            "category": "Yield Trading"
        },
        {
            "name": "GMX",
            "symbol": "GMX",
            "score": 39,
            "risk": "yellow",
            "category": "Perps"
        },
        {
            "name": "Rocket Pool",
            "symbol": "RPL",
            "score": 38,
            "risk": "yellow",
            "category": "Staking"
        }
    ]
