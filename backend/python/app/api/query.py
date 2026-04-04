from fastapi import APIRouter
from datetime import datetime
from ..schemas.schemas import AIQueryRequest, AIQueryResponse
from ai_module.analyzer import SecurityAnalyzer

router = APIRouter()
analyzer = SecurityAnalyzer()

@router.post("/", response_model=AIQueryResponse)
def query_ai(request: AIQueryRequest):
    """AI query endpoint using the advanced SecurityAnalyzer logic."""
    res = analyzer.query_response(request.query_text)
    # Map SecurityAnalyzer response to AIQueryResponse schema if necessary
    # For now, we'll return a structured response as defined in schemas
    return AIQueryResponse(
        id=1,
        query_text=request.query_text,
        ai_response=res["summary"],
        sources=res["source_attribution"], # Note: schema says List[str], res has List[Dict]. Need to align.
        timestamp=datetime.now()
    )
