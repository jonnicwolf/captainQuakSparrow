import os
import tempfile

from fastapi import APIRouter, File, UploadFile, HTTPException
from app.stt.whisper import transcribe
from app.llm.llama import ask

router = APIRouter()

@router.post("/listen")
async def listen(audio: UploadFile = File(...)):
  if not audio.filename.endswith((".wav", ".mp3", ".m4a")):
    raise HTTPException(status_code=400, detail="Unsupported file format")
  
  with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
    tmp.write(await audio.read())
    tmp_path = tmp.name

  try:
    text = transcribe(tmp_path)
    print(f"User said: {text}")
    response = ask(text)
  finally:
    os.remove(tmp_path)

  return {"response": response}