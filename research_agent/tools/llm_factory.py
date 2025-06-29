import os
from utils.config import Config
from langchain.chat_models import ChatOpenAI
from langchain_anthropic import ChatAnthropic

try:
    import google.generativeai as genai
except ImportError:
    genai = None

def get_llm(provider="openai", model=""):
    if provider == "anthropic":
        return ChatAnthropic(
            model=model or "claude-3-opus-20240229",
            anthropic_api_key=Config.ANTHROPIC_API_KEY
        )
    elif provider == "gemini":
        if genai is None:
            raise ImportError("Please install google-generativeai")
        genai.configure(api_key=Config.GEMINI_API_KEY)

        class GeminiWrapper:
            def __init__(self):
                self.model = genai.GenerativeModel("gemini-pro")

            def invoke(self, input):
                res = self.model.generate_content(input)
                return res.text

            def __call__(self, input, **kwargs):
                return self.invoke(input)

        return GeminiWrapper()
    else:
        return ChatOpenAI(openai_api_key=Config.OPENAI_API_KEY)
