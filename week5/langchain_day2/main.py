from chains import requirements_analyzer_chain

from memory import (
    save_interaction,
    get_formatted_history
)

session_id = "user_1"

requirement = """
Build an enterprise authentication platform with:
- OAuth2 login
- JWT refresh token rotation
- MFA support
- password reset
- rate limiting
- audit logging
- fraud detection
"""

# Load previous conversation
history = get_formatted_history(session_id)

# Add history into current request
enhanced_requirement = f"""
Previous Context:
{history}

Current Requirement:
{requirement}
"""

try:

    result = requirements_analyzer_chain.invoke({
        "text": enhanced_requirement
    })

    save_interaction(
        session_id,
        requirement,
        str(result.model_dump())
    )

    print("\n==============================")
    print("AI REQUIREMENTS ANALYZER")
    print("==============================\n")

    print(result.model_dump())

except Exception as e:

    print("\n[ERROR] Analysis failed\n")

    print(str(e))