import streamlit as st

from gtts import gTTS
from io import BytesIO
sound_file = BytesIO()
tts = gTTS('Add text-to-speech to your app', lang='en')
tts.write_to_fp(sound_file)


#Process this file in e.g. Streamlit.

st.audio(sound_file)