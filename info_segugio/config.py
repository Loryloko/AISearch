import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    LLM_MODEL = "gpt-4.1-mini"
    LLM_MODEL_LOW = "gpt-4.1-mini"
    AI_API_URL = "https://api.openai.com/v1/"
    OPENAI_KEY = os.getenv("OPENAI_API_KEY")

    TAVILY_KEY = os.getenv("TAVILY_API_KEY")