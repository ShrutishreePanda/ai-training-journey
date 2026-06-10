Complete Graph structure

GRAPH:  IntentRouter
STATE:  IntentState
TYPE:   Branching Tree (Fan-out, No Fan-in)
NODES:  4 (1 router + 3 handlers)
EDGES:  6 (1 entry + 1 conditional + 3 exits)
PATHS:  3 possible, 1 active per execution

┌──────────────────────────────────────────────────────┐
│                                                      │
│         START                                        │
│           │                                          │
│           │ unconditional                            │
│           ▼                                          │
│      ┌─────────┐                                     │
│      │ router  │  classifies intent                  │
│      └─────────┘                                     │
│           │                                          │
│           │ conditional edge                         │
│           │ (reads state["intent"])                  │
│           │                                          │
│     ┌─────┴──────┬──────────────┐                   │
│     │            │              │                    │
│     ▼            ▼              ▼                    │
│ ┌────────┐  ┌────────┐  ┌──────────┐               │
│ │greeting│  │  math  │  │ general  │               │
│ └────────┘  └────────┘  └──────────┘               │
│     │            │              │                    │
│     └────────────┴──────────────┘                   │
│                  │                                   │
│                  ▼                                   │
│                 END                                  │
│                                                      │
└──────────────────────────────────────────────────────┘


Node Responsibility Map:
┌─────────────────────────────────────────────────────────┐
│ NODE: router                                            │
├─────────────────────────────────────────────────────────┤
│ RESPONSIBILITY:  Classification only                    │
│ READS:           state["user_message"]                  │
│ WRITES:          state["intent"]                        │
│ KNOWS ABOUT:     keyword lists                          │
│ DOES NOT KNOW:   what handlers exist                    │
│ DOES NOT KNOW:   what handlers do                       │
│ DOES NOT KNOW:   what the final result will be          │
│ CAN IT FAIL?     Only if user_message is missing        │
├─────────────────────────────────────────────────────────┤
│ SINGLE JOB:      Set the label. Nothing else.           │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│ NODE: greeting                                          │
├─────────────────────────────────────────────────────────┤
│ RESPONSIBILITY:  Greeting response generation           │
│ READS:           state["user_message"]                  │
│ WRITES:          state["result"]                        │
│ KNOWS ABOUT:     greeting subtypes (morning/evening)    │
│ DOES NOT KNOW:   how routing was decided                │
│ DOES NOT KNOW:   math_node or general_node exist        │
│ DOES NOT KNOW:   what happens after it returns          │
│ CAN IT FAIL?     No — always has a fallback response    │
├─────────────────────────────────────────────────────────┤
│ SINGLE JOB:      Generate greeting. Nothing else.       │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│ NODE: math                                              │
├─────────────────────────────────────────────────────────┤
│ RESPONSIBILITY:  Arithmetic computation                 │
│ READS:           state["user_message"]                  │
│ WRITES:          state["result"]                        │
│ KNOWS ABOUT:     token parsing, operators, numbers      │
│ DOES NOT KNOW:   how routing was decided                │
│ DOES NOT KNOW:   greeting_node or general_node exist    │
│ CAN IT FAIL?     Protected by try/except                │
├─────────────────────────────────────────────────────────┤
│ SINGLE JOB:      Calculate and return. Nothing else.    │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│ NODE: general                                           │
├─────────────────────────────────────────────────────────┤
│ RESPONSIBILITY:  General knowledge responses            │
│ READS:           state["user_message"]                  │
│ WRITES:          state["result"]                        │
│ KNOWS ABOUT:     responses dictionary, fallback pattern │
│ DOES NOT KNOW:   how routing was decided                │
│ DOES NOT KNOW:   greeting_node or math_node exist       │
│ CAN IT FAIL?     No — always has a fallback response    │
├─────────────────────────────────────────────────────────┤
│ SINGLE JOB:      Look up or generate answer. Nothing else│
└─────────────────────────────────────────────────────────┘