import tweepy
from typing import Optional, Dict
from config import settings
import logging

logger = logging.getLogger(__name__)

class TwitterService:
    def __init__(self):
        if settings.TWITTER_BEARER_TOKEN:
            self.client = tweepy.Client(bearer_token=settings.TWITTER_BEARER_TOKEN)
        else:
            self.client = None
            logger.warning("Twitter bearer token not configured")
    
    async def get_user_by_username(self, username: str) -> Optional[Dict]:
        """Get Twitter user data by username"""
        if not self.client:
            return None
        
        try:
            # Remove @ if present
            username = username.lstrip("@")
            
            user = self.client.get_user(
                username=username,
                user_fields=["public_metrics", "description", "created_at"]
            )
            
            if user.data:
                return user.data
            return None
        except Exception as e:
            logger.error(f"Error fetching Twitter user: {e}")
            return None
    
    async def search_project_handle(self, project_name: str) -> Optional[str]:
        """Search for a project's Twitter handle"""
        if not self.client:
            return None
        
        try:
            query = f"{project_name} crypto"
            users = self.client.search_recent_tweets(
                query=query,
                max_results=10,
                tweet_fields=["author_id"]
            )
            
            # This is simplified - in production, you'd want more sophisticated matching
            if users.data and len(users.data) > 0:
                user_id = users.data[0].author_id
                user = self.client.get_user(id=user_id)
                if user.data:
                    return user.data.username
            return None
        except Exception as e:
            logger.error(f"Error searching Twitter handle: {e}")
            return None
    
    async def get_social_metrics(self, project_name: str, twitter_handle: Optional[str] = None) -> Dict:
        """Get social media metrics"""
        if not self.client:
            return {}
        
        try:
            # If no handle provided, try to find it
            if not twitter_handle:
                twitter_handle = await self.search_project_handle(project_name)
            
            if not twitter_handle:
                return {}
            
            user_data = await self.get_user_by_username(twitter_handle)
            if not user_data:
                return {}
            
            metrics = user_data.public_metrics if hasattr(user_data, 'public_metrics') else {}
            
            # Calculate engagement rate (simplified)
            followers = metrics.get("followers_count", 0)
            tweets = metrics.get("tweet_count", 1)
            engagement_rate = (metrics.get("like_count", 0) / tweets / followers * 100) if followers > 0 else 0
            
            return {
                "twitter_followers": followers,
                "twitter_engagement_rate": round(engagement_rate, 2),
                "tweet_count": tweets,
                "following": metrics.get("following_count", 0),
            }
        except Exception as e:
            logger.error(f"Error fetching social metrics: {e}")
            return {}
    
    async def get_sentiment_score(self, project_name: str) -> float:
        """Analyze sentiment of recent tweets about the project"""
        if not self.client:
            return 0.0
        
        try:
            # Search for recent tweets about the project
            query = f"${project_name} OR #{project_name} crypto -is:retweet"
            tweets = self.client.search_recent_tweets(
                query=query,
                max_results=100,
                tweet_fields=["public_metrics"]
            )
            
            if not tweets.data:
                return 0.0
            
            # Simplified sentiment based on engagement
            # In production, use proper sentiment analysis
            total_score = 0
            for tweet in tweets.data:
                metrics = tweet.public_metrics if hasattr(tweet, 'public_metrics') else {}
                likes = metrics.get("like_count", 0)
                retweets = metrics.get("retweet_count", 0)
                score = (likes + retweets * 2) / 10
                total_score += min(score, 10)
            
            return round(total_score / len(tweets.data), 2)
        except Exception as e:
            logger.error(f"Error calculating sentiment: {e}")
            return 0.0
