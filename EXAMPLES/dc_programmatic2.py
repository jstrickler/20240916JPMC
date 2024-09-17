from dataclasses import make_dataclass

Person = make_dataclass('Person',
    [
        ('first_name', str),
        ('last_name', str),
        ('age', int)
    ]
)

p1 = Person("Amanda", "Rodriguez", 85)
p2 = Person("John", "Smith", 47)

print(f"{p1 = }")
print(f"{p2 = }")
