# Assessment Recommendation Agent

## Features

- FastAPI
- Gemini 2.5 Flash
- FAISS Vector Search
- Sentence Transformers
- Product Catalog
- RAG Architecture

## Install

```bash
pip install -r requirements.txt
```

## Build Vector Database

```bash
python embed.py
```

## Start Server

```bash
uvicorn app:app --reload
```

## Swagger

http://127.0.0.1:8000/docs

## Health

GET /health

## Chat

POST /chat