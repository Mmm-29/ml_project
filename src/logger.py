import logging
import os
from  datetime import datetime
LOG_FILE="{}.log".format(datetime.now().strftime('%m_%d_%Y_%H_%M_%S'))
log_path=os.path.join(os.getcwd(),"logs",LOG_FILE) #cwd is current working directory
os.makedirs(log_path,exist_ok=True)
LOG_FILE_PATH=os.path.join(log_path,LOG_FILE)
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

