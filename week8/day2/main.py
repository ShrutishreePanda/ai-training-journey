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


#Router Node: intent_router_node - determines the intent of the user input
# It checks for keywords to classify the input as a greeting, math query, or general question
def intent_router_node(state: IntentState) -> dict:
    message = state["user_message"].lower().strip()
    
    greeting_keywords = ["hello", "hi", "hey", "greetings", "good morning", "good afternoon", "good evening"]
    math_keywords = ["calculate", "what is", "solve", "compute", "+", "-", "*", "/"]
    
    for keyword in greeting_keywords:
        if keyword in message:
            return {"intent": "greeting"}
    
    for keyword in math_keywords:
        if keyword in message:
            return {"intent": "math"}
    
    return {"intent": "general"}

#Routing function: decide_next_node - determines the next node to execute based on the identified intent
def decide_next_node(state: IntentState) -> str:
    intent= state["intent"]

    if intent == "greeting":
        return "greeting"
    elif intent == "math":
        return "math"
    else:
        return "general"

#Handler Nodes for each intent type
#Greeting Handler Node: greeting_handler_node - generates a greeting response
def greeting_handler_node(state: IntentState) -> dict:
    message = state["user_message"].lower().strip()

    if "good morning" in message:
        response = "Good morning! How can I assist you today?"
    elif "good afternoon" in message:
        response = "Good afternoon! What can I do for you?"
    elif "good evening" in message:
        response = "Good evening! How may I help you?"
    elif any(word in message for word in ["hello", "hi", "hey", "greetings"]):
        response = "Hello! How can I assist you today?"
    else:
        response = "Hi there! How can I help you?"
    
    return {"result": response}

#Math Handler Node: math_handler_node - processes simple math queries
def math_handler_node(state: IntentState) -> dict:
    message = state["user_message"].strip()

    try:
        numbers = []
        tokens = message.split()

        operator = None
        for token in tokens:
            if token in ["+", "-", "*", "/"]:
                operator = token
            else:
                try:
                    numbers.append(float(token))
                except ValueError:
                    continue
        
        if len(numbers) == 2 and operator:
            a, b = numbers[0], numbers[1]
            if operator == "+":
                answer = a + b
                result = f"The result of {a} + {b} is {answer}"
            elif operator == "-":
                answer = a - b
                result = f"The result of {a} - {b} is {answer}"
            elif operator == "*":
                answer = a * b
                result = f"The result of {a} * {b} is {answer}"
            elif operator == "/":
                if b != 0:
                    answer = a / b
                    result = f"The result of {a} / {b} is {answer}"
                else:
                    result = "Error: Division by zero is not allowed."
            else:
                result = "Sorry, I couldn't understand the math operation."
        else:
            result = "Sorry, I couldn't parse the math query. Please provide a simple expression like 'calculate 2 + 2'."
    
    except Exception as e:
        result = f"An error occurred while processing your math query: {str(e)}"
    
    return {"result": result}

#General Handler Node: general_handler_node - provides a default response for unrecognized intents
def general_handler_node(state: IntentState) -> dict:
    message = state["user_message"].lower().strip()

    responses = {
        "what is ai": (
            "AI stands for Artificial Intelligence — "
            "the simulation of human intelligence by machines."
        ),
        "what is langgraph": (
            "LangGraph is a framework for building "
            "stateful, graph-based AI workflows."
        ),
        "what is python": (
            "Python is a high-level programming language "
            "known for simplicity and readability."
        ),
        "who are you": (
            "I am an Intent Router built with LangGraph. "
            "I can handle greetings, math, and general queries!"
        ),
    }

    for key, response in responses.items():
        if key in message:
            return {"result": response}

    return {
        "result": (
            f"You asked: '{state['user_message']}'. "
            "I understand this is a general query. "
            "In production, an LLM would answer this!"
        )
    }