# SHL Assessment Recommendation System

An AI-powered assessment recommendation system built using **FastAPI**, **Google Gemini**, **FAISS**, and **Sentence Transformers**. The application recommends suitable SHL assessments based on job descriptions, required skills, and hiring requirements using Retrieval-Augmented Generation (RAG).

---

## Features

- AI-powered assessment recommendations
- Retrieval-Augmented Generation (RAG)
- Semantic search using FAISS
- Google Gemini for natural language responses
- FastAPI REST API
- Conversation-based recommendations
- Prompt injection protection
- Deployable using Docker and Render

---

## Tech Stack

- Python 3.12
- FastAPI
- Google Gemini 2.5 Flash
- Sentence Transformers (all-MiniLM-L6-v2)
- FAISS
- Docker
- Render

---

## Project Structure

```
shl-assessment-recommender/
│
├── app.py
├── chatbot.py
├── retriever.py
├── embed.py
├── config.py
├── models.py
├── requirements.txt
├── Dockerfile
├── render.yaml
├── README.md
│
├── data/
│   └── catalog.json
│
└── vectorstore/
    ├── index.faiss
    └── metadata.pkl
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/hemanth-t11/shl-assessment-recommender.git

cd shl-assessment-recommender
```

Create virtual environment

```bash
python -m venv venv
```

Activate virtual environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file

```text
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

---

## Build Vector Database

Generate embeddings and FAISS index

```bash
python embed.py
```

---

## Run Application

```bash
uvicorn app:app --reload
```

The application runs at

```
http://127.0.0.1:8000
```

Swagger UI

```
http://127.0.0.1:8000/docs
```

---

## API Endpoints

### Health Check

```
GET /health
```

Response

```json
{
  "status": "ok"
}
```

---

### Chat Endpoint

```
POST /chat
```

Example Request

```json
{
  "messages": [
    {
      "role": "user",
      "content": "I need an assessment for a Java Backend Developer with 3 years experience."
    }
  ]
}
```

Example Response

```json
{
  "reply": "Based on your hiring requirements, I recommend...",
  "recommendations": [
    {
      "name": "Assessment Name",
      "url": "Assessment URL",
      "test_type": "Assessment Category"
    }
  ],
  "end_of_conversation": false
}
```

---

## Architecture

```
User Query
      │
      ▼
 FastAPI API
      │
      ▼
Semantic Retrieval (FAISS)
      │
      ▼
Relevant SHL Assessments
      │
      ▼
Google Gemini
      │
      ▼
Recommended Assessments
```

---

## Retrieval-Augmented Generation (RAG)

1. User submits a hiring requirement.
2. Query is converted into an embedding.
3. FAISS retrieves the most relevant SHL assessments.
4. Retrieved assessments are provided as context to Gemini.
5. Gemini generates a grounded recommendation based only on the retrieved assessments.

---

## Deployment

The application is containerized using Docker and deployed on Render.

### Live API

```
https://shl-assessment-recommender-ful2.onrender.com
```

### Swagger Documentation

```
https://shl-assessment-recommender-ful2.onrender.com/docs
