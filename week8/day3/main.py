from typing import Annotated
from typing import TypedDict

from langchain_core.tools import tool
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage, SystemMessage

from langchain_openai import ChatOpenAI

from langgraph.graph import StateGraph, START, END
from langgraph.graph import ToolNode
from langgraph.graph.message import add_messages

class AgentState(TypedDict):
    messages: Annotated[list, add_messages]

@tool
def calculator(expression: str) -> str:
    """Calculate a mathematical expression."""
    try:
        allowed_characters = set('0123456789+-*/(). ')
        if not all(c in allowed_characters for c in expression):
            return "Error: Invalid characters in expression"
        
        result = eval(expression)
        return str(round(result, 4))
    except ZeroDivisionError:
        return "Error: Division by zero"
    except SyntaxError:
        return "Error: Invalid syntax in expression"
    except Exception as e:
        return f"Error: {e}"

@tool
def get_date() -> str:
    """Get the current date."""
    from datetime import datetime
    now = datetime.now()
    return now.strftime(
        "%A, %B %d, %Y at %I:%M %p"
    )

@tool
def knowledge_lookup(query: str) -> str:
    """Look up general knowledge information."""
    knowledge_base = {
        "langgraph": (
            "LangGraph is a framework for building "
            "stateful, graph-based AI agent workflows. "
            "It extends LangChain with nodes, edges, "
            "and shared state management."
        ),
        "langchain": (
            "LangChain is a framework for building "
            "LLM-powered applications. It provides "
            "tools, chains, and agents for AI development."
        ),
        "python": (
            "Python is a high-level programming language "
            "known for readability and simplicity. "
            "Widely used in AI, data science, and web development."
        ),
        "ai": (
            "Artificial Intelligence (AI) is the simulation "
            "of human intelligence by machines. It includes "
            "machine learning, deep learning, and reasoning systems."
        ),
        "llm": (
            "Large Language Models (LLMs) are AI models trained "
            "on vast text data. Examples: GPT-4, Claude, Gemini. "
            "They power modern AI assistants and agents."
        ),
        "agent": (
            "An AI agent is a system that combines an LLM with "
            "tools and a reasoning loop. It decides which tools "
            "to use and when to stop based on the task."
        ),
    }

    query_lower = query.lower().strip()

    for key, value in knowledge_base.items():
        if key in query_lower:
            return value
        
    return (
        f"No specific information found for '{query}'. "
        "In production, this would query a vector database or search engine for relevant results."
    )