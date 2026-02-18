from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()


class ChatMessage(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    messages: list[ChatMessage]
    use_rag: bool = True


@router.post("/")
def chat(body: ChatRequest):
    # TODO: tenant; optional RAG context; LLM call; audit log
    raise HTTPException(501, "Not implemented: set LLM_API_KEY for chatbot")


@router.get("/history")
def chat_history(limit: int = 50):
    raise HTTPException(501, "Not implemented")
