import openai
from openai import OpenAI
import os
from dotenv import load_dotenv
import wave
import streamlit as st

load_dotenv()
# os.environ['OPENAI_API_KEY'] = ''
openai.api_key = st.secrets['OPENAI_API_KEY'],

client = OpenAI()

class Config:
    channels = 2
    sample_width = 2
    sample_rate = 44100

def save_wav_file(file_path, wav_bytes):
    with wave.open(file_path, 'wb') as wav_file:
        wav_file.setnchannels(Config.channels)
        wav_file.setsampwidth(Config.sample_width)
        wav_file.setframerate(Config.sample_rate)
        wav_file.writeframes(wav_bytes)

def transcribe(file_path):
    audio_file = open(file_path, 'rb')
    transcription = client.audio.transcriptions.create(model="whisper-1", file=audio_file, response_format='text')
    print(transcription)
    return transcription

