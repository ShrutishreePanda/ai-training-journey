from typing import TypedDict
from langgraph.graph import StateGraph, START, END

# TypeDict: state schema
# StateGraph: graph class and start/end: built-in nodes/switches

#Defining the state schema for the graph using TypedDict
class GreetingState(TypedDict):
    name: str
    cleaned_name: str
    greeting: str


#Writing the nodes

#Node 1: name_cleaner_node - takes the raw name input and cleans it
# It removes extra spaces and capitalizes the first letter of each word
# It returns a dictionary with the cleaned name
def name_cleaner_node(state: GreetingState) -> dict:
    raw_name = state["name"]
    cleaned = raw_name.strip().title()
    return {"cleaned_name": cleaned}

#Node 2: greeting_generator_node - takes the cleaned name and generates a greeting message
# It constructs a greeting string using the cleaned name and returns it in a dictionary
def greeting_generator_node(state: GreetingState) -> dict:
    cleaned_name = state["cleaned_name"]
    greeting = f"Hello {cleaned_name}, welcome to AI Lab!"
    return {"greeting": greeting}

#Create the graph
graph_builder = StateGraph(GreetingState)

#Register nodes
graph_builder.add_node("name_cleaner", name_cleaner_node)
graph_builder.add_node("greeting_generator", greeting_generator_node)

#Define edges
graph_builder.add_edge(START, "name_cleaner")
graph_builder.add_edge("name_cleaner", "greeting_generator")
graph_builder.add_edge("greeting_generator", END)

#Compile
graph = graph_builder.compile()

if __name__ == "__main__":
    test_names=[
        "  john smith  ",
        "alice johnson"
    ]

#Run the graph and extract the results
for name in test_names:
    result = graph.invoke({"name": name})
    print(f"Input Name: '{name}'")
    print(f"Output: '{result['greeting']}'")
    print("-" * 40)

#See the full state
print(result)