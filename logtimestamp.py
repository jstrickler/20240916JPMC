from datetime import datetime
from functools import wraps
import logging


logging.basicConfig(
    level=logging.DEBUG,
    filename="timestamps.log",
)

def logtimestamp(original_function):

    @wraps(original_function)
    def replacement_function(*args, **kwargs):
        timestamp = datetime.now().ctime()
        logging.debug("Function %s called at %s", original_function.__name__, timestamp)
        return_value = original_function(*args, **kwargs)
        return return_value

    return replacement_function

