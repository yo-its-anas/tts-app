# app.py

import streamlit as st
import logging
import IPython.display as ipd
from TTS.api import TTS

# Set logging level to WARNING to suppress INFO and DEBUG logs
logging.getLogger('TTS').setLevel(logging.WARNING)

# Load the TTS model
tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC")

# Streamlit app title
st.title("Text to Speech Application")

# Text input for the user
text_input = st.text_area("Enter the text you want to convert to speech:", 
                           "Hello! Welcome to your Text to Speech application.")

# Button to generate speech
if st.button("Generate Speech"):
    output_filename = "output.wav"
    tts.tts_to_file(text=text_input, file_path=output_filename)
    st.success(f"Audio saved as {output_filename}")
    
    # Play the generated audio
    audio_file = open(output_filename, 'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/wav')

# Run the app
if __name__ == "__main__":
    st.write("Use the text area above to enter the text and click on 'Generate Speech'.")
