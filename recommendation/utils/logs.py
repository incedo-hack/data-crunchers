from utils.utility import Singleton
import logging
import os


class Logger(metaclass=Singleton):
    def __init__(self):
        self.log_level = os.environ.get('LOG_LEVEL', 'INFO').upper()

    def get_logger(self):
        logger = logging.getLogger()
        logger.setLevel(logging.getLevelName(self.log_level))
        return logger
