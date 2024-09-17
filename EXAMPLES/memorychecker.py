import os
import psutil

class MemoryChecker():
    """
    Callable class to get current memory use of program.

    Instances of this class may be called, at which time
    they will return current memory use.
    """

    def __init__(self):
        self.process = psutil.Process(os.getpid())  # Get PID of current process

    def __call__(self):
        return self.process.memory_info().rss  # Return memory use for PID

    def foo(self):
        print("foo foo foo")

if __name__ == '__main__':
    mc = MemoryChecker()
    print(mc())  # can call at any time to get current memory use
    mc.foo()
    big_data = [True] * 10_000_000
    print(mc())  # MemoryChecker.__call__(mc)  OR  mc.__call__()