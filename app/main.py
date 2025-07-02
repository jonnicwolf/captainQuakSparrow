from fastapi import FastAPI

import tempfile

app = FastAPI()

@app.post("/listen")
async def listen(audio: UploadFile = File(...)):
  with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
    tmp.write(await audio.read())
    tmp_path = tmp.name
    return "yo"