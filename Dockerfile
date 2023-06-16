FROM python:3.11-alpine

RUN apk add --no-cache gcc g++ musl-dev python3-dev ffmpeg sox git

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "-m", "vkreborn"]
