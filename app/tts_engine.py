from TTS.api import TTS
import os, uuid

OUTPUT_DIR = "outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

tts = TTS(
  model_name="tts_models/multilingual/multi-dataset/xtts_v2",
  gpu=False  # Render has no GPU
)

def generate_tts(text, speaker_wavs, language="en"):
  output_path = os.path.join(OUTPUT_DIR, f"{uuid.uuid4()}.wav")

  tts.tts_to_file(
    text=text,
    speaker_wav=speaker_wavs,
    language=language,
    file_path=output_path
  )

  return output_path
