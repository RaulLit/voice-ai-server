from fastapi import FastAPI, UploadFile, File, HTTPException
from typing import List
from fastapi.responses import FileResponse

from app.storage import save_voice_files, get_user_voice_files
from app.tts_engine import generate_tts
from app.models import TTSRequest

app = FastAPI(title="Personal Voice AI")

@app.post("/upload-voice")
async def upload_voice(user_id: str, files: List[UploadFile] = File(...)):
  if not files:
    raise HTTPException(400, "No files uploaded")

  paths = save_voice_files(user_id, files)
  return {"message": "Voice uploaded", "files": paths}

@app.post("/generate-tts")
async def generate(req: TTSRequest):
  voice_files = get_user_voice_files(req.user_id)
  if not voice_files:
      raise HTTPException(404, "Voice not found")

  output = generate_tts(req.text, voice_files, req.language)
  return FileResponse(output, media_type="audio/wav", filename="voice.wav")
