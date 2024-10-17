import logging

# Define the log file name
LOG_FILE = "info.txt"

# Set up the logging configuration
def setup_logging():
    # Create a logger
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)  # Set the logging level

    # Create a file handler to log to a file
    file_handler = logging.FileHandler(LOG_FILE, mode='w')
    file_handler.setFormatter(logging.Formatter("%(asctime)s - %(message)s"))

    # Create a stream handler to log to the console
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(logging.Formatter("%(asctime)s - %(message)s"))

    # Add the handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

setup_logging()

if __name__ == "__main__":
    logging.info("bye bye...")