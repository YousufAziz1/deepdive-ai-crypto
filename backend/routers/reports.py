from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
from typing import List
import os
import logging

from config import settings
from models.schemas import AnalysisResponse
from services.report_service import ReportService

router = APIRouter()
logger = logging.getLogger(__name__)
report_service = ReportService()

@router.post("/generate-report")
async def generate_report(analysis: AnalysisResponse):
    """
    Generate PDF report from analysis data
    
    Returns PDF file for immediate download
    """
    try:
        filename = report_service.generate_report(analysis)
        filepath = os.path.join(settings.REPORTS_DIR, filename)
        
        return FileResponse(
            filepath,
            media_type="application/pdf",
            filename=f"{analysis.project_data.project_name}_analysis.pdf"
        )
    except Exception as e:
        logger.error(f"Error generating report: {e}")
        raise HTTPException(status_code=500, detail=f"Report generation failed: {str(e)}")

@router.get("/reports")
async def list_reports() -> List[str]:
    """
    List all generated reports
    
    Returns list of available report filenames
    """
    try:
        reports_dir = settings.REPORTS_DIR
        if not os.path.exists(reports_dir):
            return []
        
        reports = [f for f in os.listdir(reports_dir) if f.endswith('.pdf')]
        return sorted(reports, reverse=True)  # Most recent first
    except Exception as e:
        logger.error(f"Error listing reports: {e}")
        return []

@router.get("/reports/{filename}")
async def download_report(filename: str):
    """
    Download a specific report
    
    Returns PDF file for download
    """
    try:
        filepath = os.path.join(settings.REPORTS_DIR, filename)
        
        if not os.path.exists(filepath):
            raise HTTPException(status_code=404, detail="Report not found")
        
        return FileResponse(
            filepath,
            media_type="application/pdf",
            filename=filename
        )
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error downloading report: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/reports/{filename}")
async def delete_report(filename: str):
    """
    Delete a specific report
    
    Removes report from storage
    """
    try:
        filepath = os.path.join(settings.REPORTS_DIR, filename)
        
        if not os.path.exists(filepath):
            raise HTTPException(status_code=404, detail="Report not found")
        
        os.remove(filepath)
        return {"status": "success", "message": f"Report {filename} deleted"}
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error deleting report: {e}")
        raise HTTPException(status_code=500, detail=str(e))
