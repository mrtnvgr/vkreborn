FROM python:3.11-alpine

RUN apk add --no-cache poetry gcc g++ musl-dev python3-dev ffmpeg sox

WORKDIR /app

COPY pyproject.toml poetry.lock ./

ENV POETRY_VIRTUALENVS_CREATE=false
RUN poetry install

COPY . .

CMD ["poetry", "run", "python", "-m", "vkreborn"]
