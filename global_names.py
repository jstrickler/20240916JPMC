"""
Some examples of using globals()
"""
person = "Taylor Swift"

def spam():
    print("SPAM!")

class Ham():
    pass

g = globals()
print(f"{g = }\n")

print(f"{__name__ = }")

p = g['person']
print(f"{p = }\n")

g['color'] = 'green'

print(f"{color = }\n")

g['bark'] = lambda: print("woof! woof!")

bark()

del g['person']

print(f"{person = }\n")







