# Voice Assistant Application
This is a simple Python-based Voice Assistant that listens for wake words and executes commands accordingly. It is designed to run in a loop, listening for activation and deactivation commands, and executing tasks based on recognized commands.

## Features
- Continuously listens for a wake word to activate the assistant.
- Upon activation, the assistant listens for commands and executes them.
- Supports custom commands and exceptions.
- Logs each command and execution status.
- Gracefully handles errors using custom exceptions.

## Key Voice Commands
"Activate Assistant": Initiates active listening for voice commands.
"Stop the Assistant": Ends the assistant's execution gracefully.
"Deactivate Assistant": Returns to the standby mode for wake word listening after completing a session of command execution.

## Project Structure
AI-Voice-Assistant/
│
├── Assistant/
│   ├── Assistant_Code/
│   │   ├── __init__.py                  # Package initializer
│   │   ├── speech_test.py               # VoiceAssistant class for handling speech recognition
│   │   ├── speak_test.py                # Function for text-to-speech (speak function)
│   │   ├── commands.py                  # Contains the execute_command function for processing commands
│   │
│   ├── Assistant_Info/
│   │   ├── __init__.py                  # Package initializer
│   │   ├── exception.py                 # Custom exception handling (CustomException class)
│   │   ├── logger.py                    # Logging setup for debugging and tracking commands
│
├── main.py                              # Main entry point for running the assistant
├── requirements.txt                     # List of dependencies required (e.g., SpeechRecognition, pyttsx3)
├── README.md                            # Project documentation and usage instructions
└── .gitignore                           # Optional: Files and directories to ignore in version control

### Files Explained:

- **`speech_test.py`**: Contains the `VoiceAssistant` class that manages listening for wake words and commands.
- **`speak_test.py`**: Contains the `speak()` function, which converts text into speech.
- **`commands.py`**: Handles the execution of specific commands recognized by the assistant.
- **`exception.py`**: Defines a `CustomException` class for handling errors specific to the assistant.
- **`logger.py`**: Configures the logging setup to track and log recognized commands and system activity.

## How to Run

1. Clone this repository to your local machine.
2. Install the necessary dependencies (e.g., `speech_recognition`, `pyttsx3`, etc.):
   ```bash
   pip install -r requirements.txt

# Run the main script
python main.py