from typing import TypedDict
from langgraph.graph import StateGraph, END

from agents.structuring_agent import run_structuring_agent
from tools.document_compiler import save_markdown_file

class AgentState(TypedDict):
    """
    Defines the structure of the state that flows through the graph.
    """
    raw_text : str
    user_request : str
    formatted_content : str
    final_document_path : str
    
# ---- Build the Graph ---
graph_builder = StateGraph(AgentState)

# --- Define the nodes ---
graph_builder.add_node("structuring_agent", run_structuring_agent)
graph_builder.add_node("file_compiler" , save_markdown_file)

# Define the workflow edges
graph_builder.set_entry_point("structuring_agent")
graph_builder.add_edge("structuring_agent", "file_compiler")
graph_builder.add_edge("file_compiler" , END)

document_agent_graph = graph_builder.compile()
