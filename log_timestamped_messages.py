""" Program to log messages with timestamps to a file """
from datetime import datetime
def log_message(message, log_file):
    """Log a message with a timestamp to a log file."""
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(log_file, 'a') as file:
        file.write(f"[{timestamp}] {message}\n")
    print(f"Logged message: {message}") 
log_file = 'app.log'