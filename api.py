from fastapi import FastAPI
from fastapi.responses import JSONResponse
from Schemas.Create_User_validator import User_validator
from Schemas.Create_Chat_validator import Chat_validator
from core.Create_Users_db import Create_Users
from core.Create_Chat_db import Create_Chats
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Dear AI an AI Based Mental health Companion"}

@app.get("/health")
def health():
    return {
        "Status": "OK",
        "Model": "Gemini 2.5 Pro",
        "Version": "1.0.0",
    }

@app.post("/Create_user")
def Create_User(user: User_validator):
    try:
        user_data = {
            "FirstName": user.FirstName,
            "LastName": user.LastName,
            "Age": user.Age,
            "Gender": user.Gender,
            "City": user.City,
            "Username": user.Username
        }
        Create_Users(user_data)
        return {"message": "User created successfully"}
    except Exception as e:
        return JSONResponse(status_code=500, content={str(e)})
    
@app.post("/Create_chat")
def Create_chat(chat: Chat_validator):
    chat_data = {
        "Chat_Name": chat.Chat_Name,
        "User_id": chat.User_id, 
    }

    Create_Chats(chat_data)
    return{"message": "Chat created successfully"}