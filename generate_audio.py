import pyttsx3
from pydub import AudioSegment
import os

def generate_audio(text, output_path='media/audio.mp3'):
    temp_wav = 'media/temp.wav'

    engine = pyttsx3.init()
    engine.setProperty('rate', 135)  # slower rate (default is ~200)
    engine.save_to_file(text, temp_wav)
    engine.runAndWait()

    # Convert WAV to MP3
    sound = AudioSegment.from_wav(temp_wav)
    sound.export(output_path, format='mp3')
    os.remove(temp_wav)
