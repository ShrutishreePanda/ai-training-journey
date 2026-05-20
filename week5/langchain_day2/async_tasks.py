import asyncio

from chains import requirements_analyzer_chain

# ============================================
# Async Single Analysis
# ============================================

async def analyze_requirement(text: str):

    result = await requirements_analyzer_chain.ainvoke({
        "text": text
    })

    return result.model_dump()

# ============================================
# Parallel Batch Analysis
# ============================================

async def analyze_multiple(requirements):

    tasks = [
        analyze_requirement(req)
        for req in requirements
    ]

    results = await asyncio.gather(*tasks)

    return results


# ============================================
# Main Async Runner
# ============================================

async def main():

    requirements = [

        """
        Build OAuth authentication system
        with MFA and JWT rotation.
        """,

        """
        Build scalable payment gateway
        supporting 1 million users.
        """,

        """
        Build AI chatbot with memory
        and session management.
        """
    ]

    results = await analyze_multiple(requirements)

    print("\n==============================")
    print("ASYNC BATCH ANALYSIS")
    print("==============================\n")

    for idx, result in enumerate(results, start=1):

        print(f"\n--- RESULT {idx} ---\n")

        print(result)


if __name__ == "__main__":

    asyncio.run(main())