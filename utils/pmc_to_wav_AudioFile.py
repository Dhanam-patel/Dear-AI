import wave
import io

def pcm_to_wav_bytes(pcm_bytes, channels=1, sampwidth=2, framerate=24000):
    wav_io = io.BytesIO()
    with wave.open(wav_io, 'wb') as wav_file:
        wav_file.setnchannels(channels)
        wav_file.setsampwidth(sampwidth)  
        wav_file.setframerate(framerate)
        wav_file.writeframes(pcm_bytes)
    wav_io.seek(0)
    return wav_io.read()
