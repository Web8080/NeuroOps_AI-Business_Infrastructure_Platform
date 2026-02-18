from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()


class RAGQuery(BaseModel):
    query: str
    top_k: int = 5


class IngestBody(BaseModel):
    document_id: str
    text: str
    metadata: dict | None = None


@router.post("/query")
def query_rag(body: RAGQuery):
    # TODO: tenant from JWT; load FAISS index; embed query; return top_k chunks + sources
    raise HTTPException(501, "Not implemented: set OPENAI_API_KEY or local embedding for RAG")


@router.post("/ingest")
def ingest_document(body: IngestBody):
    # TODO: chunk text; embed; add to FAISS index for tenant; async via Celery optional
    raise HTTPException(501, "Not implemented")


@router.get("/status/{job_id}")
def ingest_status(job_id: str):
    raise HTTPException(501, "Not implemented")
