FROM python:3.13-slim-bookworm

RUN apt update && apt install -y curl
RUN curl -sSL https://install.python-poetry.org | python3 -

ENV PATH="/root/.local/bin:${PATH}"

WORKDIR /app
COPY . /app
RUN poetry install

CMD ["poetry", "run", "local"]
