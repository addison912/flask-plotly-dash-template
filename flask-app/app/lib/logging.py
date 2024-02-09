import logging
from logging.handlers import RotatingFileHandler

handler = RotatingFileHandler('app.log', maxBytes=100000, backupCount=3)
error_logger = logging.getLogger(__name__)
error_logger.setLevel(logging.ERROR)
error_logger.addHandler(handler)
