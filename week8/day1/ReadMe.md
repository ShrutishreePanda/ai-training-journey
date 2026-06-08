LangGraph fundamentals


  TypedDict          →  State schema (the contract)
  Functions          →  Nodes (the workers)
  add_node()         →  Registration (giving workers IDs)
  add_edge()         →  Wiring (defining who works after whom)
  START / END        →  Entry and exit sentinels
  compile()          →  Validation and build
  invoke()           →  Execution trigger
  result             →  Complete final state