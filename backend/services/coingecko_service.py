import httpx
from typing import Optional, Dict
from config import settings
import logging

logger = logging.getLogger(__name__)

class CoinGeckoService:
    BASE_URL = "https://api.coingecko.com/api/v3"
    
    def __init__(self):
        self.api_key = settings.COINGECKO_API_KEY
        
    async def search_coin(self, query: str) -> Optional[str]:
        """Search for a coin by name and return its ID"""
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(f"{self.BASE_URL}/search", params={"query": query})
                response.raise_for_status()
                data = response.json()
                
                if data.get("coins"):
                    return data["coins"][0]["id"]
                return None
        except Exception as e:
            logger.error(f"Error searching coin: {e}")
            return None
    
    async def get_coin_data(self, coin_id: str) -> Optional[Dict]:
        """Get comprehensive coin data"""
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(
                    f"{self.BASE_URL}/coins/{coin_id}",
                    params={
                        "localization": "false",
                        "tickers": "false",
                        "community_data": "true",
                        "developer_data": "true"
                    }
                )
                response.raise_for_status()
                return response.json()
        except Exception as e:
            logger.error(f"Error fetching coin data: {e}")
            return None
    
    async def get_token_metrics(self, project_name: str) -> Dict:
        """Extract token metrics from CoinGecko"""
        coin_id = await self.search_coin(project_name)
        if not coin_id:
            return {}
        
        data = await self.get_coin_data(coin_id)
        if not data:
            return {}
        
        market_data = data.get("market_data", {})
        
        return {
            "price": market_data.get("current_price", {}).get("usd"),
            "market_cap": market_data.get("market_cap", {}).get("usd"),
            "fully_diluted_valuation": market_data.get("fully_diluted_valuation", {}).get("usd"),
            "volume_24h": market_data.get("total_volume", {}).get("usd"),
            "price_change_24h": market_data.get("price_change_percentage_24h"),
            "price_change_7d": market_data.get("price_change_percentage_7d"),
        }
    
    async def get_tokenomics(self, project_name: str) -> Dict:
        """Extract tokenomics data"""
        coin_id = await self.search_coin(project_name)
        if not coin_id:
            return {}
        
        data = await self.get_coin_data(coin_id)
        if not data:
            return {}
        
        market_data = data.get("market_data", {})
        
        return {
            "total_supply": market_data.get("total_supply"),
            "circulating_supply": market_data.get("circulating_supply"),
            "max_supply": market_data.get("max_supply"),
        }
    
    async def get_contract_address(self, coin_id: str) -> Optional[str]:
        """Get contract address for a coin"""
        data = await self.get_coin_data(coin_id)
        if data and "platforms" in data:
            # Try to get Ethereum contract address
            platforms = data.get("platforms", {})
            return platforms.get("ethereum") or next(iter(platforms.values()), None)
        return None
