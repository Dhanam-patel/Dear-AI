from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from AI_Pipeline.model import model
from AI_Pipeline.prompt import Prompt
from core.Update_Conversations import Update_Conversations
load_dotenv()

def model_chatting(data: str, chat_id: str):
    response = model.stream(Prompt(data, chat_id))
    # try:
    for chunks in response:    
            yield chunks.content








