import operator as op

def doit(func, value):
    return func(value)

def double(x):
    return x * 2

def negative(x):
    return -x

print(f"{doit(double, 10) = }")
print(f"{doit(negative, 100) = }")

my_value = 1.23
print(f"{doit(lambda x: (x * 10), my_value) = }")

print(f"{op.add(3, 4) = }")   # same as 3 + 4


