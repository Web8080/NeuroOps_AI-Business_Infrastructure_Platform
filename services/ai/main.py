"""AI service: RAG, chatbot, voice placeholder, fraud score. Async jobs via Celery."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import rag, chat, voice, fraud

app = FastAPI(title="NeuroOps AI", version="0.1.0")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])
app.include_router(rag.router, prefix="/api/v1/rag", tags=["rag"])
app.include_router(chat.router, prefix="/api/v1/chat", tags=["chat"])
app.include_router(voice.router, prefix="/api/v1/voice", tags=["voice"])
app.include_router(fraud.router, prefix="/api/v1/fraud", tags=["fraud"])


@app.get("/health")
def health():
    return {"status": "ok"}
