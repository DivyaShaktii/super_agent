from langchain.agents import initialize_agent
from tools.web_search import get_google_tool, get_serper_tool
from tools.summarizer import summarize
from tools.llm_factory import get_llm
from agents.base_agent import BaseAgent

class ReActAgent(BaseAgent):
    def __init__(self, provider="openai"):
        tools = [get_google_tool(), get_serper_tool()]
        tools.append(
            Tool(name="Summarize", func=lambda text: summarize(text, provider), description="Summarize content")
        )
        self.llm = get_llm(provider)
        self.agent = initialize_agent(tools, self.llm, agent="react-with-search", verbose=True)

    def run(self, query):
        return {"result": self.agent.run(query)}
