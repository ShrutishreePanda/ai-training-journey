from dotenv import load_dotenv
import os

from langchain_ollama import ChatOllama

load_dotenv()
print(os.getenv("OPENAI_API_KEY")[:10])

llm = ChatOllama(
    model="llama3.2"
)

response = llm.invoke("What is LangGraph?")

print(response.content)