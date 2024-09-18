
class SimpleIterator:
    def __init__(self, max_count=0):
        self._count = 0
        self._max_count = max_count

    def __iter__(self):
        return self
    
    def __next__(self):
        if self._count < self._max_count:
            self._count += 1
            return 100
        else:
            raise StopIteration
        
si = SimpleIterator(3)
# print(f"{next(si) = }")
# print(f"{next(si) = }")
# print(f"{next(si) = }")
# print(f"{next(si) = }")
for value in si:
    print(value)