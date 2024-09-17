

class Foo:
    def __len__(self):
        return 100
    

f = Foo()

print(f"{len(f) = }")
print()

class Thing:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value
    
    def __add__(self, other):
        return self.value + other.value
    
    def __str__(self):  # human-friendly
        return f"Thing-{self.value}"
    
    def __repr__(self):  # code to reproduce object
        return f"Thing({self.value})"

t1 = Thing(5)
t2 = Thing(10)

print(f"{t1 = }")
print(f"{t2 = }")

print(f"{t1 + t2 = }")
print(t1, t2)

class Wackadoodle:  # inherits from 'object'
    def __getitem__(self, index):
        return "HA HA HA"
    
    def __len__(self):
        return 1_000_000
    
w = Wackadoodle()

print(f"{w[5] = }")
print(f"{w['Python is fun!'] = }")
print(f"{len(w) = }")


#   newpath = p1 / p2 / p3

