FROM python:3.12-slim

WORKDIR /app

# Dipendenze di sistema necessarie a compilare psycopg2 (se non si usa psycopg2-binary si può omettere)
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]