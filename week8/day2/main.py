from typing import TypedDict
from langgraph.graph import StateGraph, START, END

#Defining the state schema for the graph using TypedDict

class IntentState(TypedDict):
    user_message: str
    intent: str
    greeting_response: str
    math_response: str
    general_response: str
    final_result: str
