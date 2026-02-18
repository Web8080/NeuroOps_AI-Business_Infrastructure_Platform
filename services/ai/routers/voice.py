from fastapi import APIRouter, HTTPException, UploadFile
from pydantic import BaseModel

router = APIRouter()


class VoiceResponse(BaseModel):
    text: str
    job_id: str | None = None


@router.post("/transcribe", response_model=VoiceResponse)
async def transcribe(audio: UploadFile):
    # TODO: speech-to-text; tenant-scoped; optional PyTorch/whisper or external API
    raise HTTPException(501, "Not implemented: voice agent placeholder")


@router.post("/synthesize")
def synthesize(text: str):
    # TODO: text-to-speech placeholder
    raise HTTPException(501, "Not implemented")
