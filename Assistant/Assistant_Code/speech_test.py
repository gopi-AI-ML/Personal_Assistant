import sys
import speech_recognition as sr
from Assistant.Assistant_Info.exception import CustomException

class VoiceAssistant:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    # Function to listen for the wake word
    def listen_for_wake_word(self):
        try:
            with sr.Microphone() as source:
                print("Listening for wake word ('Activate Assistant !!')...")
                self.recognizer.adjust_for_ambient_noise(source, duration=1)  # Adjust for noise
                audio = self.recognizer.listen(source)
                wake_word = self.recognizer.recognize_google(audio).lower()
                return wake_word
        except sr.UnknownValueError:
            return ""  # If nothing is recognized, return an empty string
        except Exception as e:
            raise CustomException(e, sys)
    
    def listen_for_command(self):
        """
        Listens for commands and returns recognized command as text.
        """
        try:
            with sr.Microphone() as source:
                print("Listening for commands...")
                self.recognizer.adjust_for_ambient_noise(source, duration=1)  # Adjust for background noise
                audio = self.recognizer.listen(source)
                command_text = self.recognizer.recognize_google(audio).lower()
                print(f"You said: {command_text}")
                return command_text
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand that.")
            return ""
        except Exception as e:
            raise CustomException(e, sys)

if __name__ == "__main__":
    while True:
        try:
            assistant = VoiceAssistant()
            word = assistant.listen_for_wake_word()
            if word == "activate assistant":
                assistant.listen_for_command()

        except Exception as e:
            raise CustomException(e,sys)
