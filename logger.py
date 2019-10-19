import logging
from logging.handlers import RotatingFileHandler
import os

logger = logging.getLogger()
logger.setLevel(logging.ERROR)

FILE_PATH = os.getcwd() + '/api.log'
fh = RotatingFileHandler(FILE_PATH, maxBytes=5242880, backupCount=500,
                         delay=True)
fh.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - '
                              '%(funcName)s - %(message)s',
                              datefmt='%m-%d-%Y %I:%M:%S %p')

# add formatter to handlers
ch.setFormatter(formatter)
fh.setFormatter(formatter)

# add handlers to logger
logger.addHandler(ch)
logger.addHandler(fh)
