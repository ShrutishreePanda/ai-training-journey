from langchain_community.chat_message_histories import ChatMessageHistory

# Session-based memory store
sessions = {}

def get_session_history(session_id: str):

    if session_id not in sessions:
        sessions[session_id] = ChatMessageHistory()

    return sessions[session_id]


def save_interaction(session_id: str, user_input: str, ai_output: str):

    history = get_session_history(session_id)

    history.add_user_message(user_input)

    history.add_ai_message(ai_output)


def get_formatted_history(session_id: str):

    history = get_session_history(session_id)

    return "\n".join(
        [f"{msg.type}: {msg.content}" for msg in history.messages]
    )