from fastapi import FastAPI, BackgroundTasks
from fastapi.responses import JSONResponse, StreamingResponse, Response, FileResponse
from fastapi.middleware.cors import CORSMiddleware
import os
import uvicorn
from Schemas.Create_User_validator import User_validator
from Schemas.Create_Chat_validator import Chat_create_validator
from Schemas.Chat_validator import Chat_validator
from core.Create_Users_db import Create_Users
from core.Create_Chat_db import Create_Chats
from core.Delete_Chat_db import Deleting_chats
from core.Update_Conversations import Update_Conversations
from AI_Pipeline.History_manager import Chat_History
from AI_Pipeline.audio_streaming import audio_file_stream
from AI_Pipeline.Audio_Synthesizer import audio_model_synthesize
from utils.Session_History import session_history
from utils.Streamed_data_handler import stream_with_final_action
from utils.pmc_to_wav_AudioFile import pcm_to_wav_bytes
app = FastAPI()



app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],  # your frontend URL here or use ["*"] for all origins during development
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
        "Version": "0.0.4",
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
            "Username": user.Username
        }
        Create_Users(user_data)
        return {"message": "User created successfully"}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error":str(e)})
    
@app.post("/Create/Chat")
def Create_chat(chat: Chat_create_validator):
    try:    
        chat_data = {
            "Chat_Name": chat.Chat_Name,
            "User_id": chat.User_id, 
        }

        Create_Chats(chat_data)
        return{"message": "Chat created successfully"}
    except Exception as e:
         return JSONResponse(status_code=500, content={"error": str(e)}) 

@app.post("/Chat/Text")
def chat(chat_data: Chat_validator, background_tasks: BackgroundTasks):
    try:    
        Input_Data = {
            "Chat_id" : chat_data.Chat_id,
            "User_Input" : chat_data.User_Input,
            }
        Update_Conversations("User", Input_Data)
        History_json = Chat_History(Input_Data)
        Type = "Text"
        response = stream_with_final_action(History_json, Input_Data["Chat_id"],background_tasks, Type)
        return StreamingResponse(response, media_type="text/event-stream") 
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

        
@app.post("/Chat/Voice")
def audio_chat(chat_data: Chat_validator, background_tasks: BackgroundTasks):
        Input_Data = {
            "Chat_id" : chat_data.Chat_id,
            "User_Input" : chat_data.User_Input,
            }
        Update_Conversations("User", Input_Data)
        History_json = Chat_History(Input_Data)
        Type = "Voice"
        Text_response = stream_with_final_action(History_json, Input_Data["Chat_id"],background_tasks, Type)
        
        Audio_response = audio_model_synthesize(Text_response)
        wav_audio = pcm_to_wav_bytes(Audio_response)
        return Response(content=wav_audio, media_type="audio/wav") 


@app.get("/retrieve_chats/{chat_id}")
def retrieve_chats(chat_id: str):
    try:
        history = session_history(chat_id)
        return history
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)}) 


@app.delete("/chat_delete/{chat_id}")
def delete_chat(chat_id: str):
    try:
        Deleting_chats(chat_id)
        return{"message": "Chat Session Deleted Successfully"}
    except Exception as e:
         return JSONResponse(status_code=500, content={"error": str(e)}) 
    



if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))  # fallback default port 8000
    uvicorn.run("api:app", host="0.0.0.0", port=port, reload=True)
