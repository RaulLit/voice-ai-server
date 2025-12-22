FROM python:3.10-slim

ENV COQUI_TOS_AGREED=1
ENV PYTHONUNBUFFERED=1

# System deps needed by TTS
RUN apt-get update && apt-get install -y \
  ffmpeg \
  libsndfile1 \
  git \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip \
  && pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
