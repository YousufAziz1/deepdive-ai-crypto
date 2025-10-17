from fastapi import APIRouter, HTTPException, BackgroundTasks
from typing import Dict
import logging

from models.schemas import AnalysisRequest, AnalysisResponse, ComparisonRequest, ComparisonResponse
from services.aggregation_service import AggregationService
from services.report_service import ReportService

router = APIRouter()
logger = logging.getLogger(__name__)

aggregation_service = AggregationService()
report_service = ReportService()

@router.post("/analyze", response_model=AnalysisResponse)
async def analyze_project(request: AnalysisRequest, background_tasks: BackgroundTasks):
    """
    Analyze a crypto project
    
    - **input**: Project name, contract address, or Twitter handle
    - **input_type**: Optional type specification (project_name, contract_address, twitter_handle)
    
    Returns comprehensive analysis with AI-powered insights
    """
    try:
        logger.info(f"Analyzing project: {request.input}")
        
        # Perform analysis
        analysis = await aggregation_service.analyze_project(
            request.input,
            request.input_type
        )
        
        # Generate PDF report in background
        def generate_pdf():
            try:
                filename = report_service.generate_report(analysis)
                analysis.report_url = f"/reports/{filename}"
                logger.info(f"Report generated: {filename}")
            except Exception as e:
                logger.error(f"Error generating report: {e}")
        
        background_tasks.add_task(generate_pdf)
        
        return analysis
    
    except Exception as e:
        logger.error(f"Analysis error: {e}")
        raise HTTPException(status_code=500, detail=f"Analysis failed: {str(e)}")

@router.post("/compare", response_model=ComparisonResponse)
async def compare_projects(request: ComparisonRequest, background_tasks: BackgroundTasks):
    """
    Compare 2-3 crypto projects side-by-side
    
    - **projects**: List of 2-3 project names to compare
    
    Returns comparative analysis with side-by-side metrics
    """
    try:
        if len(request.projects) < 2 or len(request.projects) > 3:
            raise HTTPException(
                status_code=400,
                detail="Please provide 2-3 projects for comparison"
            )
        
        logger.info(f"Comparing projects: {', '.join(request.projects)}")
        
        # Perform comparison
        comparison_data = await aggregation_service.compare_projects(request.projects)
        
        # Generate comparison report in background
        def generate_comparison_pdf():
            try:
                filename = report_service.generate_comparison_report(comparison_data)
                logger.info(f"Comparison report generated: {filename}")
            except Exception as e:
                logger.error(f"Error generating comparison report: {e}")
        
        background_tasks.add_task(generate_comparison_pdf)
        
        return ComparisonResponse(**comparison_data)
    
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Comparison error: {e}")
        raise HTTPException(status_code=500, detail=f"Comparison failed: {str(e)}")

@router.get("/quick-score/{project_name}")
async def get_quick_score(project_name: str) -> Dict:
    """
    Get quick score for a project without full analysis
    
    Returns basic metrics and overall score
    """
    try:
        # Simplified quick analysis
        analysis = await aggregation_service.analyze_project(project_name)
        
        return {
            "project_name": analysis.project_data.project_name,
            "total_score": analysis.scores.total,
            "risk_level": analysis.risk_flags.level,
            "price": analysis.project_data.token_metrics.price,
            "market_cap": analysis.project_data.token_metrics.market_cap
        }
    
    except Exception as e:
        logger.error(f"Quick score error: {e}")
        raise HTTPException(status_code=500, detail=f"Quick score failed: {str(e)}")
