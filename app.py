from fastapi import FastAPI
from models import ChatRequest
from retriever import retrieve
from chatbot import ask_gemini

app = FastAPI(
    title="SHL Assessment Recommendation API",
    version="1.0.0"
)


@app.get("/health")
def health():
    return {
        "status": "ok"
    }


@app.post("/chat")
def chat(request: ChatRequest):

    if not request.messages:
        return {
            "reply": "No conversation received.",
            "recommendations": [],
            "end_of_conversation": False
        }

    conversation = ""

    for msg in request.messages:
        conversation += f"{msg.role}: {msg.content}\n"

    latest = request.messages[-1].content

    blocked_words = [
        "ignore previous instructions",
        "system prompt",
        "developer message",
        "jailbreak",
        "hack",
        "ignore all instructions"
    ]

    if any(word in latest.lower() for word in blocked_words):
        return {
            "reply": "I can only help with SHL assessment recommendations.",
            "recommendations": [],
            "end_of_conversation": False
        }

    if len(latest.split()) < 3:
        return {
            "reply": "Could you tell me the role, seniority level, required skills, or assessment type you're looking for?",
            "recommendations": [],
            "end_of_conversation": False
        }

    retrieved_docs = retrieve(latest)

    reply = ask_gemini(
        latest,
        retrieved_docs,
        conversation
    )

    recommendations = []

    for item in retrieved_docs:

        recommendations.append({
            "name": item.get("name", ""),
            "url": item.get("link", ""),
            "test_type": ", ".join(item.get("keys", []))
        })

    return {
        "reply": reply,
        "recommendations": recommendations,
        "end_of_conversation": False
    }