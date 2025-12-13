from google import genai
import os

def audio_model_synthesize(text: str):
    client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
    
    # ✅ THIS IS THE ONLY WORKING FORMAT
    response = client.models.generate_content(
        model="gemini-2.0-flash-exp",
        contents=text,
        config={
            "response_modalities": ["AUDIO"],
            "speech_config": {
                "voice_config": {   
                    "prebuilt_voice_config": {
                        "voice_name": "Kore"
                    }
                }
            }
        }
    )
    return response
