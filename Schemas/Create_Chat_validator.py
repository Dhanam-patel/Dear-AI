from pydantic import BaseModel, Field, model_validator
from typing import Annotated
from datetime import datetime
from Chat_Repositories.Chat_Queries import Chat_Name_List


class Chat_validator(BaseModel):
    Chat_Name: Annotated[str, Field(..., description="A Unique name of the chat session.")]
    User_id: Annotated[int, Field(..., description="The ID of the user associated with this chat session.")]

    @model_validator(mode="before")
    def Check(cls, model):
        data = Chat_Name_List()  # {"Chats": [...], "Users": [...]}

        chats = [chat[0] if isinstance(chat, tuple) else chat for chat in data["Chats"]]
        users = [user[0] if isinstance(user, tuple) else user for user in data["Users"]]

        if model["Chat_Name"] in chats:
            raise ValueError("Chat with that name already exists")

        if model["User_id"] not in users:
            raise ValueError("User does not exist")

        return model


                
        
        