import typing as T

# static typing
#  Dog d = new Dog();
#  int x = 5;    #  int x = new int(5)

class Dog:
    pass

# dynamic typing
d = Dog()
x = 5


def times5(value: int | float) -> int | float:
    return value * 5

print(f"{times5(2) = }")
print(f"{times5(10) = }")
print(f"{times5('wombat') = }")
thing = [1, 2, 3]
print(f"{times5(thing) = }")

x = times5(50)

m: str
m = times5(88)
print(f"{m = }")

# tuple[int]
# tuple[int, ...] 
# list[str]

def foo(values: T.Iterable) -> list:
    return []


colors = ['red', 'green', 'purple', 'orange', 'brown',
'black', 'olive', 'navy', 'white', 'black',
'pink', 'chartreuse']


foo(colors)
foo(27)

color: str
color = "blue"
color = 123

class Animal:
    pass

class Bear(Animal):
    pass

class Lion(Animal):
    """King of the jungle"""
    pass

def add_to_zoo(animal: Animal):
    pass

b: Bear = Bear()
leo: Animal = Lion()
bb: Bear = Lion()

add_to_zoo(b)
add_to_zoo(leo)
add_to_zoo("walrus")

Numeric = T.Union[int, float]

def spam(x: Numeric) -> float:
    return 0

#  float T.Float

def doit(thing: T.Any) -> None:
    pass















