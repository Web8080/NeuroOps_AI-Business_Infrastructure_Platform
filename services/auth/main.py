"""Auth service: registration, login, JWT, password reset. Tenant-aware."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import auth as auth_router

app = FastAPI(title="NeuroOps Auth", version="0.1.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(auth_router.router, prefix="/api/v1/auth", tags=["auth"])


@app.get("/health")
def health():
    return {"status": "ok"}
