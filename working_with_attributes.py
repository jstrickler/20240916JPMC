from dataclasses import dataclass

@dataclass
class Person:
    first_name: str
    last_name: str
    age: int


p1 = Person(first_name="Taylor", last_name="Swift", age=35)
p2 = Person(first_name="Paul", last_name="McCartney", age=89)

print(p1.first_name, p1.last_name, "\n")

attribute_name = "first_name"
if hasattr(p1, attribute_name):
    print(getattr(p1, attribute_name))

#  .to_json()

json_method = "to_json"
if hasattr(p1, json_method):
    getattr(json_method)()
# else:
#     my_custom_json_whatever(p1)

setattr(p2, 'favorite_color', "purple")

print(f"{p2.favorite_color = }")

def bark_func(self):
    print("woof! woof!")

setattr(Person, "bark", bark_func)
p1.bark()
p2.bark()


