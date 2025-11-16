from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
model="gemini-2.5-pro",
temperature=1,
google_api_key = os.getenv("GOOGLE_API_KEY"),
streaming = True,
    )
