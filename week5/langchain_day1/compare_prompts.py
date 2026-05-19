from prompt_chains import (
    beginner_chain,
    technical_chain,
    summary_chain,
    usecase_chain,
    analogy_chain
)

topic = "Retrieval-Augmented Generation"

print("\nBEGINNER:\n")
print(beginner_chain.invoke({"topic": topic}))

print("\nTECHNICAL:\n")
print(technical_chain.invoke({"topic": topic}))

print("\nSUMMARY:\n")
print(summary_chain.invoke({"topic": topic}))

print("\nUSE CASES:\n")
print(usecase_chain.invoke({"topic": topic}))

print("\nANALOGY:\n")
print(analogy_chain.invoke({"topic": topic}))