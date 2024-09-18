from datetime import datetime
from functools import wraps

def show_timestamp(original_function):

    @wraps(original_function)
    def replacement_function(*args, **kwargs):
        timestamp = datetime.now().ctime()
        print(timestamp)
        return_value = original_function(*args, **kwargs)
        return return_value

    return replacement_function

@show_timestamp
def spam(n):   # spam = show_timestamp(spam)
    print("SPAM!" * n)

@show_timestamp
def ham():
    print("HAM!")

spam(5)
ham()

print(f"{spam.__name__ = }")
print(f"{ham.__name__ = }")
