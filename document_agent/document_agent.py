import os
from dotenv import load_dotenv

from graphs.workflow_graph import document_agent_graph

load_dotenv()

if __name__ == "__main__" :
    if not os.getenv("GOOGLE_API_KEY"):
        raise ValueError("GOOGLE_API_KEY not found in environment variables. Please set it in the .env file.")
    
    with open("./inputs/research_output.txt", "r") as f :
        input_text = f.read()

    initial_state = {
        "raw_text" : input_text,
        "user_request" :"Convert this report into a clean Markdown document. Use Headings, bullent points, and bold text to improve readability.",
        "formatted_content" : "",
        "final_document_path" : ""
    }

    print("---STARTING DOCUMENT AGENT---")

    final_state = document_agent_graph.invoke(initial_state)

    print("\n---AGENT RUN COMPLETE---")
    print(f"Final document available at: {final_state['final_document_path']}")