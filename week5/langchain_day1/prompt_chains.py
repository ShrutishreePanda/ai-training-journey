from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = ChatOllama(model="llama3")
parser = StrOutputParser()

# Chain 1 — Beginner Explanation
beginner_prompt = ChatPromptTemplate.from_messages([
    ("system", "You explain AI concepts to beginners."),
    ("human", "Explain {topic}")
])

beginner_chain = beginner_prompt | llm | parser

# Chain 2 — Technical Explanation
technical_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a senior AI architect."),
    ("human", "Explain {topic} technically")
])

technical_chain = technical_prompt | llm | parser

# Chain 3 — Short Summary
summary_prompt = ChatPromptTemplate.from_messages([
    ("system", "Give concise answers."),
    ("human", "Summarize {topic} in 3 lines")
])

summary_chain = summary_prompt | llm | parser

# Chain 4 — Real-world Use Cases
usecase_prompt = ChatPromptTemplate.from_messages([
    ("system", "You explain enterprise AI systems."),
    ("human", "Explain real-world applications of {topic}")
])

usecase_chain = usecase_prompt | llm | parser

# Chain 5 — Analogy-Based
analogy_prompt = ChatPromptTemplate.from_messages([
    ("system", "Use simple analogies."),
    ("human", "Explain {topic} using an analogy")
])

analogy_chain = analogy_prompt | llm | parser