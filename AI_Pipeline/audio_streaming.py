from AI_Pipeline.Audio_Synthesizer import audio_model_synthesize
from utils.pmc_to_wav_AudioFile import pcm_to_wav_bytes
from io import BytesIO


def audio_file_stream():
    response = audio_model_synthesize()
    pcm_bytes = response.candidates[0].content.parts[0].inline_data.data
    wav_bytes = pcm_to_wav_bytes(pcm_bytes)

    audio_io = BytesIO(wav_bytes)
    chunk_size = 1024
    while chunk := audio_io.read(chunk_size):
        yield chunk