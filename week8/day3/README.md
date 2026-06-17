AN AGENT DECIDES AT RUNTIME:
  1. What tools are available?
  2. Which tool(s) does this request need?
  3. In what order should I call them?
  4. Is the result sufficient or do I need more?
  5. When am I done?
------------------------------------------------------
Tool:
A tool is a Python function that an agent can call to interact with the world outside the LLM.
------------------------------------------------------
Tool Calling:
Tool calling is how an LLM requests that a tool be executed. LLM does not execute the tool directly —
LLM requests execution.
THE TOOL CALLING FLOW:

STEP 1: USER sends message to agent
        "What is 15 × 12?"

STEP 2: AGENT NODE sends message + tool list to LLM
        LLM receives:
          - User message: "What is 15 × 12?"
          - Available tools: [calculator, date_tool, knowledge]
          - Instruction: "Use tools to answer"

STEP 3: LLM DECIDES it needs calculator
        LLM does NOT calculate itself
        LLM returns a TOOL CALL REQUEST:
          {
            "tool_name": "calculator",
            "arguments": {"expression": "15 * 12"}
          }

STEP 4: TOOL EXECUTOR NODE receives the request
        Finds calculator function
        Calls calculator("15 * 12")
        Gets result: "180"

STEP 5: Result sent back to LLM
        LLM generates final response:
          "15 × 12 = 180"

STEP 6: Final response returned to user
--------------------------------------------------------
Tool Selection:
Tool selection is the LLM's decision about which tool to use given the user's request.
TOOLS AVAILABLE:
  1. calculator  — math operations
  2. get_date    — current date/time
  3. knowledge   — knowledge base lookup

USER: "What is today's date?"
LLM selects: get_date ✅

USER: "What is 15% of 2500?"
LLM selects: calculator ✅

USER: "What is today's date and 15% of 2500?"
LLM selects: get_date THEN calculator ✅

USER: "What is the capital of France?"
LLM selects: knowledge ✅

USER: "Hello!"
LLM selects: NO TOOL — answer directly ✅
---------------------------------------------------------------
Agent Loop:
The agent doesn't run once and stop. It loops until the task is complete.

>>>Annotated lets you attach metadata to a type.