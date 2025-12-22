from pydantic import BaseModel

class TTSRequest(BaseModel):
  user_id: str
  text: str
  language: str = "en"
