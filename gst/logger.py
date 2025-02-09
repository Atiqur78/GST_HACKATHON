import os
from datetime import datetime
import logging


main_dir = r"D:\GST_HACKATHON"

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_path = os.path.join(main_dir,"logs", LOG_FILE)

os.makedirs(log_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(log_path, LOG_FILE)

logging.basicConfig(filename=LOG_FILE_PATH, 
                    level= logging.INFO,
                    format="[ %(asctime)s %(name)s - %(levelname)s - %(message)s]",
                    )