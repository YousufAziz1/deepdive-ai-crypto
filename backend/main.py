from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

from config import settings
from routers import analysis, projects, reports
from models.schemas import HealthResponse

app = FastAPI(
    title="DeepDive AI - Crypto Research Agent",
    description="AI-powered crypto project analysis using Sentient ROMA",
    version="1.0.0"
)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create reports directory if it doesn't exist
os.makedirs(settings.REPORTS_DIR, exist_ok=True)

# Mount static files for reports
app.mount("/reports", StaticFiles(directory=settings.REPORTS_DIR), name="reports")

# Include routers
app.include_router(analysis.router, prefix="/api/v1", tags=["Analysis"])
app.include_router(projects.router, prefix="/api/v1", tags=["Projects"])
app.include_router(reports.router, prefix="/api/v1", tags=["Reports"])

@app.get("/", response_model=HealthResponse)
async def root():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "service": "DeepDive AI - Crypto Research Agent",
        "version": "1.0.0"
    }

@app.get("/api/v1/health", response_model=HealthResponse)
async def health_check():
    """Detailed health check"""
    return {
        "status": "healthy",
        "service": "DeepDive AI",
        "version": "1.0.0"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG
    )
