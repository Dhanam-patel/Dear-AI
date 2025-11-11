from Chat_Repositories.Chat_Context import Retrieve_Chat_History
import json

def session_history(data: str):
    chat_history_tuples = Retrieve_Chat_History(data)
    chat_history = [
        {
            "conv_id": content[0],
            "role": content[1],
            "content": content[2],
            "metadata": content[3],
            "created_at": content[4].isoformat() if content[4] else None,
            "chat_id": content[5],
        }
        for content in chat_history_tuples
    ]
    return chat_history
