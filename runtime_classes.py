
class Cat:
    def meow(self):
        print("meow meow")

c1 = Cat()
c2 = Cat()
c2.meow()

class Animal:
    pass


class_name = "Dog"

def bark(self):
    print("Woof! Woof!")

# runtime class definition
Dog = type(class_name, (Animal,), {'bark': bark, 'wag': lambda self: print("wagging")})


d1 = Dog()
d2 = Dog()
d1.bark()
d2.wag()
