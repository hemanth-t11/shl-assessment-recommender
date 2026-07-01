import google.generativeai as genai
from config import GOOGLE_API_KEY, LLM_MODEL

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel(LLM_MODEL)

SYSTEM_PROMPT = """
You are an SHL Assessment Recommendation Assistant.

Rules:
1. Recommend ONLY assessments from the retrieved SHL catalog.
2. Never invent assessments.
3. If the user query is vague, ask one clarification question.
4. Compare assessments only using the retrieved context.
5. Refuse unrelated questions politely.
6. Keep answers concise and professional.
"""


def build_context(retrieved_docs):
    context = ""

    for doc in retrieved_docs:

        context += f"""
Assessment Name: {doc.get('name', '')}

Description:
{doc.get('description', '')}

Categories:
{', '.join(doc.get('keys', []))}

Job Levels:
{', '.join(doc.get('job_levels', []))}

Languages:
{', '.join(doc.get('languages', []))}

Duration:
{doc.get('duration', '')}

Remote Testing:
{doc.get('remote', '')}

Adaptive:
{doc.get('adaptive', '')}

URL:
{doc.get('link', '')}

--------------------------------------------------
"""

    return context


def ask_gemini(user_query, retrieved_docs, conversation):

    context = build_context(retrieved_docs)

    prompt = f"""
{SYSTEM_PROMPT}

Conversation History

{conversation}

Retrieved SHL Assessments

{context}

Current User Query

{user_query}

Instructions

- Answer ONLY using the retrieved assessments.
- If insufficient information exists, ask one clarification question.
- If recommending assessments, explain why they fit.
- If comparing assessments, compare only retrieved assessments.
- Never make up assessment names or URLs.

Return a natural conversational response.
"""

    try:

        response = model.generate_content(prompt)

        return response.text

    except Exception as e:

        return f"Error communicating with Gemini: {str(e)}"