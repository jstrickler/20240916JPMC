from dataclasses import dataclass

@dataclass
class Person:
    # generates __init__()  method
    # generates __repr__() method
    first_name: str
    last_name: str
    age: int

p1 = Person(first_name="Bill", last_name="Gates", age=68)
p2 = Person(first_name="Taylor", last_name="Swift", age=35)


print(f"{p1 = }")
print(p1)
p2.first_name = "Tom"
print(f"{p2 = }")

print(dir(p1))

# print(f"{type(Person.first_name) = }")

#                 (self, ...)
# Person.__setattr__(p2, "last_name", "Jones")
# print(f"{p2 = }")

field1 = "x"
field2 = "y"

Point = type("class", (), {"x":0, "y":0})
Point = dataclass(Point)
p = Point(5, 10)



