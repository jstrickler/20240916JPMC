from datetime import datetime
from functools import wraps
import logging


logging.basicConfig(
    level=logging.DEBUG,
    filename="timestamps.log",
)

class LogTimestamp:
    def __init__(self, original_function):
        self._original_function = original_function

    def __call__(self, *args, **kwargs):
        timestamp = datetime.now().ctime()
        logging.debug("Function %s called at %s", self._original_function.__name__, timestamp)
        return_value = self._original_function(*args, **kwargs)
        return return_value

