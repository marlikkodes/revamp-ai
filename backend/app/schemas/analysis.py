from pydantic import BaseModel


class AnalyzeRequest(BaseModel):
    """Request model for the /analyze endpoint."""

    url: str


class Recommendation(BaseModel):
    """A single optimization recommendation."""

    category: str
    priority: str  # high, medium, low
    title: str
    description: str


class AnalysisResponse(BaseModel):
    """Full analysis response returned by the optimization crew."""

    overall_score: int = 0
    seo_score: int = 0
    ux_score: int = 0
    copy_score: int = 0
    performance_score: int = 0
    conversion_score: int = 0
    summary: str = ""
    recommendations: list[Recommendation] = []
