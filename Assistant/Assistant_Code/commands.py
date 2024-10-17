import os,sys
import webbrowser
from Assistant.Assistant_Info.logger import logging
from Assistant.Assistant_Info.exception import CustomException
from Assistant.Assistant_Code.speak_test import speak

def execute_command(command):
    try:
        command = command.lower()
        if "open chrome" in command:
            print("Opening Chrome...")
            speak("Opening Chrome...")
            os.startfile("chrome.exe")


        elif "close the chrome" in command:
            print("Closing Chrome...")
            speak("Closing Chrome...")
            os.system("taskkill /im chrome.exe /f")
        
        elif "open camera" in command:
            print("opening camera...")
            os.system("start microsoft.windows.camera:")
            speak("opening camera...")

        elif "close the camera" in command:
            print("Closing the camera...")
            os.system("taskkill /im WindowsCamera.exe /f")
            speak("Closing the camera...")

        elif "open notepad" in command:
            print("opening notepad")
            os.startfile("notepad.exe")
            speak("Opening Notepad...")

        elif "close the notepad" in command:
            print("Closing Notepad...")
            os.system("taskkill /im notepad.exe /f")
            speak("Closing Notepad...")

        elif "open website" in command:
            website = command.split("open website")[-1].strip()  # Get the website URL after the command
            if website:
                print(f"Opening {website}...")
                speak(f"Opening {website}...")
                # Use webbrowser to open the specified website
                webbrowser.open(f"www.{website}.com")  # Opens the website in the default web browser
            else:
                speak("Please provide a website name.")

        elif "open file explorer" in command:
            print("Opening File Explorer...")
            speak("Opening File Explorer...")
            os.startfile("explorer.exe")

        elif "close file explorer" in command:
            print("Closing File Explorer...")
            speak("Closing File Explorer...")
            os.system("taskkill /im explorer.exe /f")



    except Exception as e:
        logging.info(CustomException(e,sys))
        raise CustomException(e,sys)
