import sys
from Assistant.Assistant_Code.speech_test import VoiceAssistant
from Assistant.Assistant_Code.speak_test import speak
from Assistant.Assistant_Info.exception import CustomException
from Assistant.Assistant_Code.commands import execute_command
from Assistant.Assistant_Info.logger import logging

if __name__ == "__main__":
    speak("Running Assistant")
    try:
        assistant = VoiceAssistant()  # Initialize once outside the loop
        # while True:
        #     # Continuously listen for the wake word
        #     # wake_word = assistant.listen_for_wake_word()
        #     # print(f"Detected: {wake_word}")  # Debugging line to check what was detected

        #     # if wake_word and "activate assistant" in wake_word:
        #     text = "Hello, How can I assist you."
        #     print(text)
        #     speak(text=text)
                
        #         # Once the wake word is detected, start listening for commands
        while True:
                command = assistant.listen_for_command()
                if command:
                        # Execute the command if recognized
                    logging.info(command)
                    execute_command(command=command)

                if "deactivate assistant" in command:
                    text = "Deactivating Assistant..."
                    speak(text)
                    speak("Goodbye!")
                    break  # Exit command listening and return to wake word listening
                    
                elif "stop the assistant" in command:
                    speak("Stopping the Assistant...")
                    speak("I will be here if you run the program again")
                    break

    except Exception as e:
        raise CustomException(e, sys)