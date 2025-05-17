# backend/api/query.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from core.rag_pipeline import ask_hr_question, get_employee_stats

router = APIRouter()

# Request model
class QueryRequest(BaseModel):
    question: str

# Response model
class QueryResponse(BaseModel):
    answer: str
    sources: list[str]

# POST endpoint for querying
@router.post("/query", response_model=QueryResponse)
async def query_endpoint(req: QueryRequest):
    try:
        answer, sources = ask_hr_question(req.question)
        return {"answer": answer, "sources": sources}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
from fastapi import APIRouter
from pydantic import BaseModel
from core.rag_pipeline import ask_hr_question, get_employee_stats


router = APIRouter()

# Query model
class HRQuery(BaseModel):
    question: str
    department: str = None
    job_satisfaction: int = None

@router.post("/query")
def query_hr_assistant(payload: HRQuery):
    response = ask_hr_question(
        question=payload.question,
        department=payload.department,
        job_satisfaction=payload.job_satisfaction
    )
    return response

# ✅ ADD THIS ROUTE TO SUPPORT THE ANALYTICS DASHBOARD
@router.get("/employee-stats")
def fetch_employee_stats():
    return get_employee_stats()
