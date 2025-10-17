import httpx
from typing import Optional, Dict
import logging

logger = logging.getLogger(__name__)

class DefiLlamaService:
    BASE_URL = "https://api.llama.fi"
    COINS_URL = "https://coins.llama.fi"
    
    async def search_protocol(self, name: str) -> Optional[str]:
        """Search for a protocol by name"""
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(f"{self.BASE_URL}/protocols")
                response.raise_for_status()
                protocols = response.json()
                
                # Search for matching protocol
                for protocol in protocols:
                    if name.lower() in protocol.get("name", "").lower():
                        return protocol.get("slug")
                return None
        except Exception as e:
            logger.error(f"Error searching protocol: {e}")
            return None
    
    async def get_protocol_data(self, slug: str) -> Optional[Dict]:
        """Get protocol TVL and other data"""
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(f"{self.BASE_URL}/protocol/{slug}")
                response.raise_for_status()
                return response.json()
        except Exception as e:
            logger.error(f"Error fetching protocol data: {e}")
            return None
    
    async def get_token_holders(self, contract_address: str) -> Optional[int]:
        """Get number of token holders (if available)"""
        # DefiLlama doesn't provide holder count directly
        # This would need to be fetched from blockchain explorers like Etherscan
        return None
    
    async def get_tvl_data(self, project_name: str) -> Dict:
        """Get TVL and DeFi metrics"""
        slug = await self.search_protocol(project_name)
        if not slug:
            return {}
        
        data = await self.get_protocol_data(slug)
        if not data:
            return {}
        
        return {
            "tvl": data.get("tvl"),
            "chain_tvls": data.get("chainTvls", {}),
            "change_1d": data.get("change_1d"),
            "change_7d": data.get("change_7d"),
            "mcap_tvl_ratio": data.get("mcaptvl"),
        }
