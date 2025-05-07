import logging


class Logger:
    def __init__(self, name='AppLogger', level=logging.INFO):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)

        if not self.logger.handlers:
            console_handler = logging.StreamHandler()
            console_handler.setLevel(level)

            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

            console_handler.setFormatter(formatter)

            self.logger.addHandler(console_handler)

    def get_logger(self):
        return self.logger
