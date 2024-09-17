from collections import namedtuple


person = "Bill", "Gates", "Microsoft", "1955-10-24"

print(f"{person[1] = }")

first_name, last_name, product, dob = person

Person = namedtuple("Person", "first_name last_name product dob")

p1 = Person("Bill", "Gates", "Microsoft", "1955-10-24")
print(f"{p1 = }")
print(f"{p1.first_name = } {p1.last_name = }")


