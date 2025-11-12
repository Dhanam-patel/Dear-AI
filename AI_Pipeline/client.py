from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from AI_Pipeline.model import model
from AI_Pipeline.prompt import Prompt
load_dotenv()

def model_chatting(data: str, chat_id: str):
    response = model.invoke(Prompt(data, chat_id))
    return response







