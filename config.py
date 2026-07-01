import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

LLM_MODEL = "gemini-2.5-flash"

EMBEDDING_MODEL = "all-MiniLM-L6-v2"

TOP_K = 10