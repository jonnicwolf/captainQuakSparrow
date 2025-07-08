from faster_whisper import WhisperModel

model = WhisperModel("base", compute_type="int8")

def transcribe(audio_path: str) -> str:
  segments, _ = model.transcribe(audio_path)
  return " ".join([segment.text.strip() for segment in segments])