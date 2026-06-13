## Logger is used to log any execution that occurs within the application

import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
# Generate a unique log filename using the current date and time

logs_path = os.path.join(os.getcwd(), "logs")
# Path to the logs directory

os.makedirs(logs_path, exist_ok=True)
# Create the logs directory if it does not already exist

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)
# Full path to the log file

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s", ## This is the format we want our log to be like
    level=logging.INFO, ## So anywhere i apply logging.info it will apply this configurations
)

## For testing purposes
# if __name__=="__main__":
#     logging.info('Logging has started')

