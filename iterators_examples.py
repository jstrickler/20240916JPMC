
x = ['a', 'b', 'c']  # x is iterable but NOT iterator

for thing in x:
    print(thing)
print()

mary = open('DATA/mary.txt')   # mary is iterator AND iterable
for line in mary:  # mary.readline()
    print(line.rstrip())
print()

mary = open('DATA/mary.txt')   # mary is iterator AND iterable
line = next(mary)
print(f"{line = }")

x = ['a', 'b', 'c']  # x is iterable but NOT iterator
iter_x = iter(x)  # get an iterator for x
letter = next(iter_x)
print(f"{letter = }")
print(f"{next(iter_x) = }")

# next() gets next value of iterator
# iter() returns iterator obj from any iterable

e = enumerate(x)
print(f"{e = }")
print(f"{next(e) = }")
print(f"{next(e) = }")
print(f"{next(e) = }")
print(f"{next(e) = }")

e = enumerate(x)
for index, value in e:
    print(index, value)
