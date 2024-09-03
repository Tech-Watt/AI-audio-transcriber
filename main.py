import streamlit as st 
import os 
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()
key = os.getenv('OPENAI_API_KEY')
MODEL = 'gpt-4o'
client = OpenAI(api_key = key)



st.title('AI AUDIO Transcriber App')   
    # Upload audio file
audio_file = st.file_uploader("Upload an audio file", type=["mp3", "wav", "m4a"])
if audio_file:
    # Display audio player
    st.audio(audio_file)

    st.title('Audio Transcript')
    transcription = client.audio.transcriptions.create(
    model="whisper-1", 
    file=audio_file, 
    #response_format="text",
    prompt="provide an accurate transcription of the audio file using ponctuations and capitalization as well."
    )
    st.write(transcription.text)
