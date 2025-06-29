from agents.react_agent import ReActAgent
from agents.graph_agent import GraphAgent
from tools.image_fetcher import fetch_images

class ResearchPipeline:
    def __init__(self, mode="graph", provider="openai"):
        self.agent = GraphAgent(provider) if mode == "graph" else ReActAgent(provider)

    def research(self, query, include_images=False):
        result = self.agent.run(query)
        images = fetch_images(query) if include_images else []
        return {"result": result, "images": images}
