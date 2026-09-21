import json
import logging

from fastapi import APIRouter, HTTPException

from app.crews.optimizer_crew import create_optimizer_crew
from app.schemas.analysis import AnalysisResponse, AnalyzeRequest
from app.services.firecrawl_service import FirecrawlService

logger = logging.getLogger(__name__)

router = APIRouter()


@router.post("/analyze", response_model=AnalysisResponse)
async def analyze_website(request: AnalyzeRequest):
    """Analyze a website URL and return optimization scores and recommendations."""
    try:
        # Step 1: Scrape the website
        logger.info(f"Scraping website: {request.url}")
        service = FirecrawlService()
        content = service.scrape(request.url)

        if not content or len(content.strip()) < 50:
            raise HTTPException(
                status_code=400,
                detail="Could not extract meaningful content from the provided URL.",
            )

        # Truncate content if too long to stay within token limits
        max_chars = 15000
        if len(content) > max_chars:
            content = content[:max_chars] + "\n\n[Content truncated for analysis]"

        # Step 2: Run the optimization crew
        logger.info("Starting CrewAI optimization analysis...")
        crew = create_optimizer_crew()

        result = await crew.kickoff_async(inputs={"url": request.url, "website_content": content})

        # Step 3: Parse the result
        logger.info("Parsing crew output...")
        return _parse_crew_output(result)

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Analysis failed: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Analysis failed: {str(e)}")


def _parse_crew_output(result) -> AnalysisResponse:
    """Parse CrewAI output into an AnalysisResponse."""
    # Try the built-in structured output first
    if hasattr(result, "json_dict") and result.json_dict:
        try:
            return AnalysisResponse(**result.json_dict)
        except Exception:
            pass

    if hasattr(result, "pydantic") and result.pydantic:
        try:
            return result.pydantic
        except Exception:
            pass

    # Fall back to parsing raw text output as JSON
    raw = str(result)

    try:
        start = raw.find("{")
        end = raw.rfind("}") + 1
        if start != -1 and end > start:
            json_str = raw[start:end]
            data = json.loads(json_str)
            return AnalysisResponse(**data)
    except (json.JSONDecodeError, ValueError) as e:
        logger.warning(f"JSON parsing failed: {e}")

    # Last resort: return the raw text as the summary
    logger.warning("Could not parse structured output — returning raw summary")
    return AnalysisResponse(
        overall_score=0,
        summary=raw[:2000] if raw else "Analysis completed but output could not be structured.",
    )
