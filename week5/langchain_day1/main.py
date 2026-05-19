from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

llm = ChatOllama(model="llama3")

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a senior AI architect specializing in LLM systems, LangChain, Retrieval-Augmented Generation (RAG),"
    "AI agents, and enterprise AI workflows."),
    ("human", "Explain the AI concept: {topic}")
])

formatted_prompt = prompt.invoke({
    "topic": "Retrieval-Augmented Generation (RAG)"
})

response = llm.invoke(formatted_prompt)

print(response.content)