from abc import ABCMeta, abstractmethod

class Toast(metaclass=ABCMeta):
    @abstractmethod
    def burn(self):
        pass

class Spam(metaclass=ABCMeta):

    @abstractmethod
    def doit(self, value, thing, junk):
        pass

    def hello(self):
        print("Hello, ABC world")


class Ham(Spam):
    def doit(self):
        print("I am doing the thing...")

h = Ham()

h.hello()
h.doit()
print()

class Eggs(Ham, Toast):
    def shout(self):
        print("HELLO EVERYBODY!")

    def doit(self):
        super().doit()
        print("doing the eggs")

    def burn(self):
        print("burnt to a crisp")


e = Eggs()
e.hello()
e.doit()
e.shout()
e.burn()
print()

print(Eggs.mro())