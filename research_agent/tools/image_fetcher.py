from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from utils.config import Config

def internal_search(query, path="internal_index", top_k=5):
    db = FAISS.load_local(path, OpenAIEmbeddings(openai_api_key=Config.OPENAI_API_KEY))
    docs = db.similarity_search(query, k=top_k)
    return "\n".join(doc.page_content for doc in docs)
