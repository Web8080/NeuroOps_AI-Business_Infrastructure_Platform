# Celery app for async AI tasks (RAG ingest, long-running chat, etc.).
# Run: celery -A celery_app worker -l info
# Requires CELERY_BROKER_URL (e.g. redis://localhost:6379/1)

from celery import Celery
import os

broker = os.environ.get("CELERY_BROKER_URL", "redis://localhost:6379/1")
app = Celery("neuroops_ai", broker=broker, backend=broker)
app.conf.task_serializer = "json"
app.conf.result_serializer = "json"
app.conf.accept_content = ["json"]


@app.task(bind=True)
def rag_ingest_task(self, tenant_id: str, document_id: str, text: str):
    # TODO: chunk text, embed, add to FAISS index for tenant_id
    return {"document_id": document_id, "status": "pending"}


@app.task(bind=True)
def chat_async_task(self, tenant_id: str, session_id: str, messages: list):
    # TODO: call LLM; store result; return job_id for polling
    return {"session_id": session_id, "status": "pending"}
