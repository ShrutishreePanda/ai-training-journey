from langchain_ollama import ChatOllama

llm = ChatOllama(model="llama3")

response = llm.invoke("Explain LangChain simply")

print(response.content)