from langchain_google_genai import ChatGoogleGenerativeAI

    
model = ChatGoogleGenerativeAI(
model="gemini-2.5-pro",
temperature=1,
google_api_key = 'AIzaSyC_RPKPPP6B8JG-Bjy8-iG9C3shgDRLNo0',
streaming = True,
    )
