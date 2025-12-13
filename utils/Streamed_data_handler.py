from fastapi import BackgroundTasks
from AI_Pipeline.client import model_chatting
from core.Create_Chat_db import Create_Chats
from utils.final_response_update import final_db_update

def stream_with_final_action(history: str, input_data: dict,  background_tasks: BackgroundTasks, Type: str):
    final_output = []
    if Type == "Text":
        for chunk in model_chatting(history, input_data["Chat_id"], input_data["User_id"]):
            final_output.append(chunk)
            yield chunk 
        complete_output = ''.join(final_output)
    elif Type == "Voice":
        for chunk in model_chatting(history, input_data["Chat_id"], input_data["User_id"]):
            final_output.append(chunk)
        complete_output = ''.join(final_output)
        yield complete_output

    if input_data["User_id"] == "False":
        background_tasks.add_task(final_db_update, input_data["Chat_id"], complete_output)