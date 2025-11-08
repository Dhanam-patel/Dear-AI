from pydantic import BaseModel, Field, field_validator
from typing import Annotated, Literal
from Chat_Repositories.User_check import User_Name_List 


class User_validator(BaseModel):
    FirstName: Annotated[str, Field(...,description="The user's first name")]
    LastName: Annotated[str, Field(...,description="The user's last name")]
    Age: Annotated[int, Field(...,gt=0, description="The user's age")]
    Gender: Annotated[Literal["male", "female"], Field(...,description="The user's gender")]
    City: Annotated[str, Field(...,description="The city where the user resides")]  
    Username: Annotated[str, Field(..., description="The user's username")]

    @field_validator("FirstName", "LastName", "City")
    @classmethod
    def Validate(cls, value, mode="before"):
        return value.title()
    
    @field_validator("Gender")
    @classmethod
    def validate_gender(cls, value):
         return value.lower()

    @field_validator("Username")
    @classmethod
    def check_username(cls, value):
        user_data = User_Name_List()
        username = [user[1] if isinstance(user, tuple) else user for user in user_data["Users"]]

        if value in username:
                raise ValueError("Username already exist")
