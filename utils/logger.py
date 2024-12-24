import logging


class Logger:
    def __init__(self):
        self.logger = logging.getLogger('pageLogger')

    def get_logger(self):
        return self.logger
