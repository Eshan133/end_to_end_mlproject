import  logging   # all the executions, custom exception error should be logged
import os
from datetime import datetime 

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" # text file created in this naming convention
log_path = os.path.join(os.getcwd(), "logs", LOG_FILE) # create logs folder on current working directory -> every file will start with "logs" then the convention defined above

os.makedirs(log_path, exist_ok=True) # makes directory, and appends when it already exists

LOG_FILE_PATH = os.path.join(log_path, LOG_FILE)

# whenever we import logging.info and we write out any print messagea it will create the log following this pattern
logging.basicConfig(
    filename= LOG_FILE_PATH,
    format= "[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level= logging.INFO,
)

# Creates the log with the cmd "python src/logger.py"
'''
if __name__ == "__main__":
    logging.info("Logging has started")
'''