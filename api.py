from fastapi import FastAPI, BackgroundTasks
from fastapi.responses import JSONResponse, StreamingResponse, Response, FileResponse
from fastapi.middleware.cors import CORSMiddleware
import os
import json
import uvicorn
from Schemas.Create_User_validator import User_validator
from Schemas.Create_Chat_validator import Chat_create_validator
from Schemas.Chat_validator import Chat_validator
from core.Create_Users_db import Create_Users
from core.Create_Chat_db import Create_Chats
from core.Delete_Chat_db import Deleting_chats
from core.Update_Conversations import Update_Conversations
from Chat_Repositories.user_data import users_data
from Chat_Repositories.chat_data import chats_data
from Chat_Repositories.Chat_check import Chat_Name_List
from AI_Pipeline.History_manager import Chat_History
from AI_Pipeline.audio_streaming import audio_file_stream
from AI_Pipeline.client import model_chatting
from utils.Session_History import session_history
from utils.Streamed_data_handler import stream_with_final_action
app = FastAPI()



app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.api_route("/", methods=["GET", "HEAD"])
def home():
    return {"message": "Dear AI an AI Based Mental health Companion"}

@app.get("/health")
def health():
    return {
        "Status": "OK",
        "Model": "Gemini 2.5 Pro",
        "Version": "0.0.5",
    }

@app.post("/Create/User")
def Create_User(user: User_validator):
    try:
        user_data = {
            "FirstName": user.FirstName,
            "LastName": user.LastName,
            "Age": user.Age,
            "Gender": user.Gender,
            "City": user.City,
            "Username": user.Username,
            "Email": user.User_Email
        }
        Create_Users(user_data)
        id = users_data(user_data["Username"])
        return {"message": "User created successfully", "User_ID": id}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error":str(e)})
    
@app.post("/Create/Chat")
def Create_chat(chat: Chat_create_validator, background_tasks: BackgroundTasks):
    try:    
        chat_data = {
            "Chat_id": chat.Chat_id,
            "User_Input": chat.User_Input,
            "User_id": chat.User_id, 
        }
        Type = "Voice" 
        input_json = {"input": chat_data["User_Input"]}
        input = json.dumps(input_json)
        Title = model_chatting(input, chat_data["Chat_id"], chat_data["User_id"])
        final_output = []
        for chunk in Title:
            final_output.append(chunk)
            complete_output = ''.join(final_output)
        Create_Chats(chat_data, complete_output) 
        return{"Title": complete_output}
    except Exception as e:
         return JSONResponse(status_code=500, content={"error": str(e)}) 

@app.post("/Chat/Text")
def chat(chat_data: Chat_validator, background_tasks: BackgroundTasks):
    try:    
        Input_Data = {
            "Chat_id" : chat_data.Chat_id,
            "User_Input" : chat_data.User_Input,
            "User_id": "False"
            }
        Update_Conversations("User", Input_Data)
        History_json = Chat_History(Input_Data)
        Type = "Text"
        response = stream_with_final_action(History_json, Input_Data,background_tasks, Type)
        return StreamingResponse(response, media_type="text/event-stream") 
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

        
@app.post("/Chat/Voice")
def audio_chat(chat_data: Chat_validator, background_tasks: BackgroundTasks):
    try:
            Input_Data = {
                "Chat_id" : chat_data.Chat_id,
                "User_Input" : chat_data.User_Input,
                "User_id": "False"
                }   
            Update_Conversations("User", Input_Data)
            History_json = Chat_History(Input_Data)
            Type = "Voice"
            Text_response = stream_with_final_action(History_json, Input_Data,background_tasks, Type)
            
            Audio_response = audio_file_stream(Text_response)

            return StreamingResponse(Audio_response, media_type="audio/wav") 
    except Exception as e:
            return JSONResponse(status_code=500, content={"error": str(e)})

@app.get("/retrieve/chats/{user_id}")
def retrieve_user_chats(user_id: str):
    try:  
        Chat_data = Chat_Name_List(user_id)
        chats = [chat[0] if isinstance(chat, tuple) else chat for chat in Chat_data["Chats"]]
        return {"chats": chats}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})


@app.get("/retrieve/conversations/{chat_id}")
def retrieve_conversation(chat_id: str):
    try:
        history = session_history(chat_id)
        return history
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)}) 


@app.delete("/chat/delete/{chat_id}")
def delete_chat(chat_id: str):
    try:
        Deleting_chats(chat_id)
        return{"success": True}
    except Exception as e:
         return JSONResponse(status_code=500, content={"error": str(e)}) 
    



if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000)) 
    uvicorn.run("api:app", host="0.0.0.0", port=port, reload=True)
