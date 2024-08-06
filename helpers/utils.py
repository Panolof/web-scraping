import time
import logging

def setup_logging(log_file='scraper.log'):
    logging.basicConfig(filename=log_file, level=logging.INFO,
                        format='%(asctime)s:%(levelname)s:%(message)s')

def delay(seconds):
    time.sleep(seconds)
