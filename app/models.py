from pydantic import BaseModel, Field
from typing import List, Optional
from enum import Enum

class TaskCategory(str, Enum):
    SURVEY = "survey"
    USABILITY_TESTING = "usability_testing"
    AI_ANNOTATION = "ai_annotation"
    MICROTASK = "microtask"
    FOCUS_GROUP = "focus_group"

class RiskLevel(str, Enum):
    SAFE = "safe"
    CAUTION = "caution"
    DANGER = "danger"

class Task(BaseModel):
    id: str
    title: str
    description: str
    platform: str
    platform_url: str
    category: str
    reward_amount: float
    currency: str = "USD"
    estimated_minutes: int
    hourly_rate_usd: float
    trust_score: int = Field(ge=0, le=100)
    verified: bool = True
    payment_methods: List[str]
    eligible_countries: List[str] = ["Global"]
    min_age: int = 18
    requirements: List[str] = []
    scam_risk_level: RiskLevel = RiskLevel.SAFE
    scam_warnings: List[str] = []
    direct_apply_url: str
    date_posted: str

class Platform(BaseModel):
    id: str
    name: str
    website: str
    category: str
    trust_score: int
    avg_hourly_pay: str
    min_payout: str
    payment_methods: List[str]
    reputation: str
    pros: List[str]
    cons: List[str]
    is_verified: bool = True

class ScamCheckRequest(BaseModel):
    url: Optional[str] = None
    text_content: Optional[str] = None

class ScamCheckResponse(BaseModel):
    score: int
    verdict: str
    risk_level: RiskLevel
    is_safe: bool
    detected_red_flags: List[str]
    trust_signals: List[str]
    recommendation: str
    analysis_details: dict
