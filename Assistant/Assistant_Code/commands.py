import os
import sys
import cv2
import webbrowser
import threading
from Assistant.Assistant_Info.logger import logging
from Assistant.Assistant_Info.exception import CustomException
from Assistant.Assistant_Code.speak_test import speak

global stop_video
stop_video = False

def record_video():
    global stop_video
    speak("Capturing video...")
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        speak("Error: Could not access the camera.")
        return
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('video.avi', fourcc, 20.0, (640, 480))
    stop_video = False
    while not stop_video:
        ret, frame = cap.read()
        if not ret:
            speak("Error: Failed to capture video frame.")
            break
        out.write(frame)
        cv2.imshow('Recording Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    out.release()
    cv2.destroyAllWindows()
    speak("Video captured and saved successfully.")

def execute_command(command):
    global stop_video
    try:
        command = command.lower()
        if "open chrome" in command:
            speak("Opening Chrome...")
            os.startfile("chrome.exe")

        elif "close the chrome" in command:
            speak("Closing Chrome...")
            os.system("taskkill /im chrome.exe /f")
        
        elif "open camera" in command:
            os.system("start microsoft.windows.camera:")
            speak("Opening camera...")

        elif "capture image" in command:
            speak("Capturing Image...")
            cap = cv2.VideoCapture(0)
            if not cap.isOpened():
                speak("Error: Could not access the camera.")
                return
            ret, frame = cap.read()
            if ret:
                cv2.imwrite("photo.jpg", frame)
                speak("Photo taken and saved successfully.")
            else:
                speak("Error: Failed to capture the photo.")
            cap.release()
            cv2.destroyAllWindows()

        elif "capture video" in command:
            video_thread = threading.Thread(target=record_video)
            video_thread.start()
        
        elif "stop video recording" in command:
            stop_video = True
            speak("Stopping video recording...")

        elif "close the camera" in command:
            os.system("taskkill /im WindowsCamera.exe /f")
            speak("Closing the camera...")

        elif "open notepad" in command:
            os.startfile("notepad.exe")
            speak("Opening Notepad...")

        elif "close the notepad" in command:
            os.system("taskkill /im notepad.exe /f")
            speak("Closing Notepad...")

        elif "open website" in command:
            website = command.split("open website")[-1].strip()
            if website:
                speak(f"Opening {website}...")
                webbrowser.open(f"www.{website}.com")
            else:
                speak("Please provide a website name.")

        elif "open file explorer" in command:
            speak("Opening File Explorer...")
            os.startfile("explorer.exe")

        elif "close file explorer" in command:
            speak("Closing File Explorer...")
            os.system("taskkill /im explorer.exe /f")

    except Exception as e:
        logging.info(CustomException(e, sys))
        raise CustomException(e, sys)