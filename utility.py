import pandas as pd
from datetime import datetime
import logging
import os

#UTILITIES
log_path = r'.logs'

def setup_logging(path):
    os.makedirs(path,exist_ok=True)
    log_time = datetime.now().strftime('%Y%m%d-%H%M%S')
    log_file = os.path.join(path,f"{log_time}.log")

    logging.basicConfig(filename=log_file,level=logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s',
                        force=True)
    logging.info("Logging Setup Complete!")

if __name__ == '__main__':
    setup_logging(log_path)
    logging.info("Try")