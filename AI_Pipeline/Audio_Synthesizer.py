from google import genai
from google.genai import types


def audio_model_synthesize(Text_response: str):
        client = genai.Client(api_key="AIzaSyCf0qt7ipQvrJYZLHSFH73EnaaMEcWPtXg")

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
        data = response.candidates[0].content.parts[0].inline_data.data

        return data

