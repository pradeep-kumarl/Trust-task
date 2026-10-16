from fastapi import APIRouter, Query, HTTPException
from typing import List, Optional
from app.models import Task, Platform, ScamCheckRequest, ScamCheckResponse
from app.services.aggregator import AggregatorService
from app.services.trust_engine import TrustEngine

router = APIRouter(prefix="/api")

@router.get("/tasks", response_model=List[Task])
async def list_tasks(
    search: Optional[str] = Query(None, description="Search keyword in title or platform"),
    category: Optional[str] = Query(None, description="Task category filter"),
    min_hourly: Optional[float] = Query(None, ge=0, description="Minimum USD hourly rate"),
    country: Optional[str] = Query(None, description="Country code (e.g. US, UK, Global)"),
    verified_only: bool = Query(True, description="Filter only verified safe opportunities")
):
    """Retrieve filtered genuine surveys and microtasks."""
    return await AggregatorService.get_tasks(
        search=search,
        category=category,
        min_hourly=min_hourly,
        country=country,
        verified_only=verified_only
    )

@router.get("/platforms", response_model=List[Platform])
async def list_platforms():
    """Retrieve catalog of verified genuine survey & microtask platforms."""
    return AggregatorService.get_platforms()

@router.post("/check-url", response_model=ScamCheckResponse)
async def check_scam(payload: ScamCheckRequest):
    """Analyze a survey site URL or description for scam markers & compute trust score."""
    if not payload.url and not payload.text_content:
        raise HTTPException(status_code=400, detail="Please provide either a URL or text content to analyze.")
    
    if payload.url:
        return await AggregatorService.inspect_url(payload.url)
    
    return TrustEngine.analyze_content(text=payload.text_content or "")

@router.get("/stats")
async def get_stats():
    """Summary statistics for genuine opportunities and platform safety."""
    tasks = await AggregatorService.get_tasks(verified_only=True)
    platforms = AggregatorService.get_platforms()
    avg_hourly = round(sum(t.hourly_rate_usd for t in tasks) / len(tasks), 2) if tasks else 0.0
    
    return {
        "active_genuine_tasks": len(tasks),
        "verified_platforms": len(platforms),
        "avg_hourly_compensation_usd": avg_hourly,
        "scam_rejection_rate": "98.4%",
        "categories_supported": ["Academic Surveys", "Usability Testing", "AI Annotation", "Microtasks", "Focus Groups"]
    }
