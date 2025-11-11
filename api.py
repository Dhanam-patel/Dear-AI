from fastapi import FastAPI
from fastapi.responses import JSONResponse
import asyncio
from Schemas.Create_User_validator import User_validator
from Schemas.Create_Chat_validator import Chat_validator
from Schemas.Chat_validator import Chat_validator
from core.Create_Users_db import Create_Users
from core.Create_Chat_db import Create_Chats
from core.Delete_Chat_db import Deleting_chats
from core.Update_Conversations import Update_Conversations
from AI_Pipeline.client import model_chatting
from AI_Pipeline.History_manager import Chat_History
from utils.Session_History import session_history
app = FastAPI()


@app.api_route("/", methods=["GET", "HEAD"])
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
        return JSONResponse(status_code=500, content={"error":str(e)})
    
@app.post("/Create_chat")
def Create_chat(chat: Chat_validator):
    try:    
        chat_data = {
            "Chat_Name": chat.Chat_Name,
            "User_id": chat.User_id, 
        }

        Create_Chats(chat_data)
        return{"message": "Chat created successfully"}
    except Exception as e:
         return JSONResponse(status_code=500, content={"error": str(e)}) 

@app.post("/Chat")
def chat(chat_data: Chat_validator):
    Input_Data = {
        "Chat_id" : chat_data.Chat_id,
        "User_Input" : chat_data.User_Input,
        }
    History_json = Chat_History(Input_Data)
    Update_Conversations("User", Input_Data)
    response = model_chatting(History_json)
    Response_Data = {
        "Chat_id": chat_data.Chat_id,
        "AI_Output": f"{response.content}"
    }
    Update_Conversations("AI", Response_Data)
    return {"response": response}

@app.get("/retrieve_chats/{chat_id}")
def retrieve_chats(chat_id: str):
    history = session_history(chat_id)
    return history


@app.delete("/chat_delete/{chat_id}")
def delete_chat(chat_id: str):
    try:
        Deleting_chats(chat_id)
        return{"message": "Chat Session Deleted Successfully"}
    except Exception as e:
         return JSONResponse(status_code=500, content={"error": str(e)}) 

