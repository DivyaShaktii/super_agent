from langgraph.graph import StateGraph
from tools.web_search import get_google_tool, get_serper_tool
from tools.internal_search import internal_search
from tools.summarizer import summarize
from tools.llm_factory import get_llm
from agents.base_agent import BaseAgent

class GraphAgent(BaseAgent):
    def __init__(self, provider="openai"):
        self.provider = provider
        self.google = get_google_tool().func
        self.serper = get_serper_tool().func

    def run(self, query):
        graph = StateGraph(input_keys=["input"], output_keys=["summary"])

        @graph.node
        def search_google(state): state["web1"] = self.google(state["input"]); return state

        @graph.node
        def search_serper(state): state["web2"] = self.serper(state["input"]); return state

        @graph.node
        def search_internal(state): state["local"] = internal_search(state["input"]); return state

        @graph.node
        def combine_and_summarize(state):
            text = f"{state['web1']}\n\n{state['web2']}\n\n{state['local']}"
            state["summary"] = summarize(text, self.provider)
            return state

        graph.add_edge("search_google", "search_serper")
        graph.add_edge("search_serper", "search_internal")
        graph.add_edge("search_internal", "combine_and_summarize")

        built = graph.compile()
        return built.invoke({"input": query})
