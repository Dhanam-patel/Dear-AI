from google import genai
from google.genai import types
import os

def audio_model_synthesize(Text_response: str):
        client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

        response = client.models.generate_content(
        model="gemini-2.5-flash-preview-tts",
        contents=Text_response,
        config=types.GenerateContentConfig( 
            response_modalities=["AUDIO"],
            speech_config=types.SpeechConfig(
                voice_config=types.VoiceConfig(
                    prebuilt_voice_config=types.PrebuiltVoiceConfig(
                    voice_name='Kore',
                    )
                )
            ),
        )
        )

        return response

