import streamlit as st
from TTS.api import TTS

# Attempt to create a TTS instance
try:
    tts = TTS(model_name="tts_models/en/ljspeech/tacotron2")
except Exception as e:
    st.error(f"Error initializing TTS: {e}")

# Streamlit app code
st.title("Text to Speech App")
text_input = st.text_area("Enter text to convert to speech:")

if st.button("Convert to Speech"):
    if text_input:
        # Save the speech to a file
        tts.tts_to_file(text=text_input, file_path="output.wav")
        st.success("Speech has been saved to output.wav")
    else:
        st.error("Please enter some text.")
