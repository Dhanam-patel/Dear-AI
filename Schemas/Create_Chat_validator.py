from pydantic import BaseModel, Field, model_validator
from typing import Annotated
from Chat_Repositories.Chat_check import Chat_Name_List
from Chat_Repositories.User_check import User_Name_List

class Chat_create_validator(BaseModel):
    User_Input: Annotated[str, Field(..., description="A Unique name of the chat session.")]
    User_id: Annotated[str, Field(..., description="The ID of the user associated with this chat session.")]
    Chat_id: Annotated[str, Field(..., description="A Unique ID for the chat session.")]
    @model_validator(mode="before")
    def Check(cls, model):
        User_data = User_Name_List()

        users = [user[0] if isinstance(user, tuple) else user for user in User_data["Users"]]
        if model["User_id"] not in users:
                    raise ValueError("User does not exist")

        return model            
                

        