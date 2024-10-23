import streamlit as st
import logging

# Try importing IPython and TTS, handle the error if not installed
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

# Ensure that the TTS model can be loaded without errors
try:
    # Load the TTS model
    tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC")
except Exception as e:
    st.error(f"Error loading TTS model: {str(e)}")

# Streamlit app title
st.title("Text to Speech Application")

# Text input for the user
text_input = st.text_area("Enter the text you want to convert to speech:", 
                           "Hello! Welcome to your Text to Speech application.")

# Button to generate speech
if st.button("Generate Speech"):
    output_filename = "output.wav"
    
    # Check if TTS is initialized correctly
    if 'tts' in globals():
        try:
            # Generate speech and save to a file
            tts.tts_to_file(text=text_input, file_path=output_filename)
            st.success(f"Audio saved as {output_filename}")
            
            # Play the generated audio
            audio_file = open(output_filename, 'rb')
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format='audio/wav')
        except Exception as e:
            st.error(f"Error generating or playing the audio: {str(e)}")
    else:
        st.error("TTS model is not loaded correctly. Please check the logs for more details.")

# Run the app
if __name__ == "__main__":
    st.write("Use the text area above to enter the text and click on 'Generate Speech'.")

