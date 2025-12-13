from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=1,
    google_api_key=os.getenv("GOOGLE_API_KEY"),  # ✅ Correct (auto-reads env anyway)
    streaming=True,  # ✅ Correct parameter
)


# from langchain_groq import ChatGroq
# import os
# from dotenv import load_dotenv

# load_dotenv()

# model = ChatGroq(
#     model="llama-3.1-8b-instant",  # ⚡ Fastest free model
#     temperature=1,
#     groq_api_key=os.getenv("GROQ_API_KEY"),  # Changed key name
#     streaming=True,
# )