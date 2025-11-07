from pydantic import BaseModel, Field, field_validator
from typing import Annotated, Literal

class User_validator(BaseModel):
    FirstName: Annotated[str, Field(...,description="The user's first name")]
    LastName: Annotated[str, Field(...,description="The user's last name")]
    Age: Annotated[int, Field(...,gt=0, description="The user's age")]
    Gender: Annotated[Literal["male", "female"], Field(...,description="The user's gender")]
    City: Annotated[str, Field(...,description="The city where the user resides")]  
    Username: Annotated[str, Field(...,min_length=5, description="The user's username")]

    @field_validator("FirstName", "LastName", "Gender", "City")
    @classmethod
    def Validate(cls, value, mode="before"):
        return value.title()

