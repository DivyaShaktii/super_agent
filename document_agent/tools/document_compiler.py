import os

def save_markdown_file(state : dict) -> dict :
    """
    Saves the formatted content to a Markdown file.
    Args :
       state (dict): The current state of the graph.

    Returns:
        dict: A dictionary containing the path to the final document.
    """

    print("---SAVING DOCUMENT---")
    content = state["formatted_content"]
    
    # Define the output path
    output_dir = "./outputs/documents"
    os.makedirs(output_dir, exist_ok=True)
    file_path = os.path.join(output_dir, "Formatted_Report.md")

    # Write the content to the file
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
        
    print(f"---DOCUMENT SAVED AT: {file_path}---")

    return {"final_document_path": file_path}