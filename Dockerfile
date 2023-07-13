FROM python:3.11-alpine

RUN apk add --no-cache ffmpeg sox git

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY vkreborn vkreborn

CMD ["python", "-m", "vkreborn"]
