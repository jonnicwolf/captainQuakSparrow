import os
import tempfile

from fastapi import APIRouter, File, UploadFile
from app.stt.whisper import transcribe

router = APIRouter()

@router.post("/listen")
async def listen(audio: UploadFile = File(...)):
  with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
    tmp.write(await audio.read())
    tmp_path = tmp.name

  text = transcribe(tmp_path)
  os.remove(tmp_path)
  return {"transcription": text}