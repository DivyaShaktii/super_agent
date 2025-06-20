from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI



def run_structuring_agent(state : dict) -> dict :
    """
    Invokes the structuring agent to convert raw text to Markdown.

    Args:
        state (dict): The current state of the graph.

    Returns:
        dict: A dictionary with the formatted markdown content.
    """

    llm = ChatGoogleGenerativeAI(model = "gemini-2.5-flash" , temperature = 0)

    print("---DRAFTING MARKDOWN---")
    raw_text = state["raw_text"]
    user_request = state["user_request"]

    prompt_template = ChatPromptTemplate.from_messages(
        [
            ("system", "You are an expert technical writer. Your task is to transform raw text into a well-structured and easy-to-read document."),
            ("user", "Based on the following user request and raw text, please generate a final, polished document in Markdown format.\n\n"
                     "USER REQUEST: {request}\n\n"
                     "---RAW TEXT---\n"
                     "{text}")
        ]
    )

    chain = prompt_template | llm

    formatted_content = chain.invoke({"request": user_request, "text": raw_text})

    return {"formatted_content": formatted_content.content}