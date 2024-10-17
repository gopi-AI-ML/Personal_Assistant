import pyttsx3
import os
import sys
from Assistant.Assistant_Info.exception import CustomException

current = os.getcwd()

def speak(text, filename="output.mp3"):
    try:
        engine = pyttsx3.init()
        # Get available voices
        voices = engine.getProperty('voices')

        # Set the voice to male (voices[0]) or female (voices[1])
        engine.setProperty('voice', voices[1].id)  # Change to voices[0] for male

        # Adjust speaking rate (default is around 200 words per minute)
        engine.setProperty('rate', 150)  # Slow down the rate to 150 words per minute

        # Adjust volume (range: 0.0 to 1.0)
        engine.setProperty('volume', 1.0)  # Set to max volume

        # Speak the text
        engine.say(text)

        audio_dir = "audio"
        if not os.path.exists(audio_dir):
            os.makedirs(audio_dir)
        os.chdir(audio_dir)
        
        engine.save_to_file(text,filename)
        engine.runAndWait()

        os.chdir(current)

    except Exception as e:
        raise CustomException(e, sys)

if __name__ == "__main__":
    speak(text="Hello, I am your AI assistant.")