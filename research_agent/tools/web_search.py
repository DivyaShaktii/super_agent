import os
from langchain.tools import Tool
from langchain.utilities import GoogleSearchAPIWrapper
from langchain_community.utilities import GoogleSerperAPIWrapper
from utils.config import Config

def get_google_tool():
    os.environ["GOOGLE_API_KEY"] = Config.GOOGLE_API_KEY
    os.environ["GOOGLE_CSE_ID"] = Config.GOOGLE_CSE_ID
    google = GoogleSearchAPIWrapper()
    return Tool(name="GoogleSearch", func=google.run, description="Google search")

def get_serper_tool():
    os.environ["SERPER_API_KEY"] = Config.SERPER_API_KEY
    serper = GoogleSerperAPIWrapper()
    return Tool(name="SerperSearch", func=serper.run, description="Serper search")
