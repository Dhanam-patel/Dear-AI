from core.Update_Conversations import Update_Conversations


def final_db_update(chat_id: str, complete_text: str):
    Response_Data = {
        "Chat_id": chat_id,
        "AI_Output": complete_text
    }
    Update_Conversations("AI", Response_Data)