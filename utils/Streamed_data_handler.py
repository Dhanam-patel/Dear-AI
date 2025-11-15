from fastapi import BackgroundTasks
from AI_Pipeline.client import model_chatting
from utils.final_response_update import final_db_update

def stream_with_final_action(history: str, chat_id: str,  background_tasks: BackgroundTasks):
    final_output = []

    for chunk in model_chatting(history, chat_id):
        final_output.append(chunk)
        yield chunk 

    complete_output = ''.join(final_output)
    background_tasks.add_task(final_db_update, chat_id, complete_output)
