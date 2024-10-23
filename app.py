import streamlit as st
import logging

# Attempt to import necessary modules with error handling
try:
    import IPython.display as ipd
except ImportError:
    st.error("IPython is not installed. Please install it using 'pip install ipython'.")

try:
    from TTS.api import TTS
except ImportError:
    st.error("TTS module is not installed. Please install it using 'pip install TTS'.")

# Set logging level to WARNING to suppress INFO and DEBUG logs
logging.getLogger('TTS').setLevel(logging.WARNING)

# Try to load the TTS model and handle errors if they occur
try:
    tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC")
except Exception as e:
    tts = None
    st.error(f"Error loading TTS model: {str(e)}")

# Streamlit app title
st.title("Text to Speech Application")

# Text input for the user
text_input = st.text_area("Enter the text you want to convert to speech:", 
                           "Hello! Welcome to your Text to Speech application.")

# Button to generate speech
if st.button("Generate Speech"):
    output_filename = "output.wav"
    
    if tts:  # Check if the TTS model loaded successfully
        try:
            # Generate speech and save it to a file
            tts.tts_to_file(text=text_input, file_path=output_filename)
            st.success(f"Audio saved as {output_filename}")
            
            # Play the generated audio
            audio_file = open(output_filename, 'rb')
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format='audio/wav')
        except Exception as e:
            st.error(f"Error generating or playing the audio: {str(e)}")
    else:
        st.error("TTS model is not loaded properly. Please check the logs.")

# Run the app
if __name__ == "__main__":
    st.write("Use the text area above to enter the text and click on 'Generate Speech'.")
