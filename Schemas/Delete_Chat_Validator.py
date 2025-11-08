from pydantic import BaseModel, Field, model_validator
from typing import Annotated
from Chat_Repositories.Chat_check import Chat_Name_List
class Delete_Chat_DB(BaseModel):
    Chat_id = Annotated[str, Field(..., description="The chat Id of the user ")]
    
    @model_validator
    def chat_deleted(cls, model):
        Chat_data = Chat_Name_List()
        chats = [chat[0] if isinstance(chat, tuple) else chat for chat in Chat_data["Chats"]]

        if model.Chat_id in chats:
            return model        
        raise ValueError("Chat does not exist")