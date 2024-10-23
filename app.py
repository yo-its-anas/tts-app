import streamlit as st
import logging
from TTS.api import TTS
from io import BytesIO

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
    # Generate speech and save it to a BytesIO object
    output_buffer = BytesIO()
    tts.tts_to_file(text=text_input, file_path=output_buffer)

    # Rewind the buffer
    output_buffer.seek(0)

    # Play the generated audio
    st.audio(output_buffer, format='audio/wav')

    st.success("Speech generated and played successfully!")

# Run the app
if __name__ == "__main__":
    st.write("Use the text area above to enter the text and click on 'Generate Speech'.")
