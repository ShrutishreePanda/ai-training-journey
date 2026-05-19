from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

print("Starting model...")

llm = ChatOllama(model="llama3")

prompt = ChatPromptTemplate.from_messages([
    ("system", """
    You are a senior AI architect specializing in AI systems.
    """),

    ("human", "Explain the following topic: {topic}")
])

parser = StrOutputParser()

print("Building chain...")

chain = prompt | llm | parser

topic = input("Enter topic: ")

print("Invoking chain...")

result = chain.invoke({
    "topic": topic
})

print("Received output...\n")

print(result)