from pydantic import BaseModel, Field, computed_field
from typing import Annotated

class Chat_validator(BaseModel):
    Chat_id : Annotated[str, Field(..., description=("ID of chat session"))]
    User_Input : Annotated[str, Field(..., description=("The Input given by the User"))]




