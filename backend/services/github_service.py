from github import Github
from typing import Optional, Dict, List
from config import settings
import logging

logger = logging.getLogger(__name__)

class GitHubService:
    def __init__(self):
        self.client = Github(settings.GITHUB_TOKEN) if settings.GITHUB_TOKEN else None
    
    async def search_repository(self, project_name: str) -> Optional[str]:
        """Search for a repository by project name"""
        if not self.client:
            logger.warning("GitHub token not configured")
            return None
        
        try:
            repos = self.client.search_repositories(query=project_name, sort="stars", order="desc")
            if repos.totalCount > 0:
                return repos[0].full_name
            return None
        except Exception as e:
            logger.error(f"Error searching repository: {e}")
            return None
    
    async def get_repository_metrics(self, repo_name: str) -> Dict:
        """Get comprehensive repository metrics"""
        if not self.client:
            return {}
        
        try:
            repo = self.client.get_repo(repo_name)
            
            # Get commit activity
            commits = repo.get_commits()
            recent_commits = 0
            try:
                from datetime import datetime, timedelta
                one_month_ago = datetime.now() - timedelta(days=30)
                for commit in commits:
                    if commit.commit.author.date > one_month_ago:
                        recent_commits += 1
                    else:
                        break
            except:
                recent_commits = 0
            
            # Get last commit date
            last_commit = None
            try:
                last_commit_obj = commits[0]
                last_commit = last_commit_obj.commit.author.date.isoformat()
            except:
                pass
            
            return {
                "github_stars": repo.stargazers_count,
                "github_forks": repo.forks_count,
                "commits_last_month": recent_commits,
                "contributors": repo.get_contributors().totalCount,
                "last_commit_date": last_commit,
                "open_issues": repo.open_issues_count,
                "watchers": repo.watchers_count,
            }
        except Exception as e:
            logger.error(f"Error fetching repository metrics: {e}")
            return {}
    
    async def get_technical_metrics(self, project_name: str) -> Dict:
        """Get technical development metrics"""
        repo_name = await self.search_repository(project_name)
        if not repo_name:
            return {}
        
        return await self.get_repository_metrics(repo_name)
