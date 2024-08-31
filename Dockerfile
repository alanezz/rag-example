FROM python:3.12-slim

# Upgrade pip
RUN pip install --no-cache-dir --upgrade pip

# Install poetry
RUN pip install -U poetry

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN poetry install

COPY /src ./src

CMD ["poetry", "run", "python", "src/search.py"]
