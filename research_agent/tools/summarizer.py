from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from tools.llm_factory import get_llm

def summarize(text, provider="openai"):
    llm = get_llm(provider)
    prompt = PromptTemplate.from_template("Summarize this:\n{text}")
    chain = LLMChain(llm=llm, prompt=prompt)
    return chain.run(text=text)
