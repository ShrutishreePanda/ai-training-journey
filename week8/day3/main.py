from typing import Annotated
from typing import TypedDict

from langchain_core.tools import tool
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage, SystemMessage

from langchain_openai import ChatOpenAI

from langgraph.graph import StateGraph, START, END
from langgraph.graph import ToolNode
from langgraph.graph.message import add_messages

#Defining the state schema for the graph using TypedDict
class AgentState(TypedDict):
    messages: Annotated[list, add_messages]

#Tool Nodes for the agent
#Calculator Tool Node: calculator_tool_node - performs mathematical calculations
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

#Date Tool Node: date_tool_node - provides the current date and time
@tool
def get_date() -> str:
    """Get the current date."""
    from datetime import datetime
    now = datetime.now()
    return now.strftime(
        "%A, %B %d, %Y at %I:%M %p"
    )

# FORMAT CODES:
#   %A → Full weekday: "Monday"
#   %B → Full month: "June"
#   %d → Day: "08"
#   %Y → Year: "2026"
#   %I → 12-hour: "02"
#   %M → Minutes: "30"
#   %p → AM/PM: "PM"

# RESULT: "Monday, June 08, 2026 at 02:30 PM"


#Knowledge Lookup Tool Node: knowledge_lookup_tool_node - provides general knowledge information
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

#LLM setup for the agent
tools = [calculator, get_date, knowledge_lookup]
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# bind_tools() converts your @tool functions into OpenAI function-calling JSON schema and attaches it to every API request:
#bind_tools creates a new LLM instance that is aware of the tools and can invoke them when needed.
#This allows the agent to seamlessly integrate tool usage into its responses based on the system prompt guidelines.
llm_with_tools = llm.bind_tools(tools)

#Agent Nodes
#  System prompt appears exactly ONCE at the beginning of every conversation no matter how many loop iterations run

System_Prompt = """You are a helpful assistant with access to three tools:

1. calculator — use for any math operations
2. get_date   — use for date/time questions
3. knowledge_lookup — use for factual questions

Guidelines:
- Use tools when needed, answer directly when possible
- For math: always use the calculator tool
- For dates: always use get_date tool
- Be concise and clear in responses
"""
# The system prompt provides instructions to the agent on how to use the tools effectively. It emphasizes when to use each tool and encourages concise responses.
# In a production system, this prompt would be carefully crafted and iteratively improved to ensure the agent behaves as desired.
# The agent will refer to this prompt to understand its capabilities and how to respond to user queries appropriately.
def agent_node(state: AgentState) -> dict:
    messages = state["messages"]

    # Ensure the system prompt is included at the start of the conversation
    if not any(isinstance(msg, SystemMessage) for msg in messages):
        messages = [SystemMessage(content=System_Prompt)] + messages
    
#This is where intelligence happens
#     WHAT HAPPENS DURING invoke():

# 1. LangChain serializes messages to OpenAI format:

# 2. HTTP POST to OpenAI API:

# 3. OpenAI processes and returns:

# 4. LangChain converts to AIMessage:

# 5. Returns this AIMessage to agent_node
    response = llm_with_tools.invoke(messages)
    return {"messages": [response]}

#Router Node: router_node - routes user messages to the appropriate handler based on intent
#LLM classifies itself via response structure and the decision is just detected
#Routing function
def should_continue(state: AgentState) -> str:
    last_message = state["messages"][-1]

    if last_message.tool_calls:
        return "tools"
    else:
        return "end"