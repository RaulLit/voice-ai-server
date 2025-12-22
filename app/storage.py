import os
import shutil

VOICE_DIR = "voices"
os.makedirs(VOICE_DIR, exist_ok=True)

def save_voice_files(user_id: str, files):
  user_path = os.path.join(VOICE_DIR, user_id)
  os.makedirs(user_path, exist_ok=True)

  saved_files = []

  for file in files:
    file_path = os.path.join(user_path, file.filename)
    with open(file_path, "wb") as buffer:
      shutil.copyfileobj(file.file, buffer)
    saved_files.append(file_path)

  return saved_files

def get_user_voice_files(user_id: str):
  user_path = os.path.join(VOICE_DIR, user_id)
  if not os.path.exists(user_path):
    return []
  return [os.path.join(user_path, f) for f in os.listdir(user_path)]
