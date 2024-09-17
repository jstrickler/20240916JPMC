from dataclasses import dataclass, field

field_specs = [
    ("first_name", str),
    ("last_name", str),
    ("age", int),
]

fields = {}  # data fields
annotations = {}
for field_name, field_type in field_specs:
    fields[field_name] = field()
    annotations[field_name] = field_type

Person = type("Person", (), fields)
Person.__annotations__ = annotations

Person = dataclass(Person)  # decorate the class

p1 = Person("Amanda", "Rodriguez", 85)
p2 = Person("John", "Smith", 47)

print(f"{p1 = }")
print(f"{p2 = }")
