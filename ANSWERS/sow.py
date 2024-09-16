from functools import singledispatch


class Pig:
    def grunt(self):
        print("grunt grunt grunt")


class Seed:

    def grow(self):
        print('....growing......')


@singledispatch
def sow(arg):
    pass


@sow.register
def _(arg: Pig):
    arg.grunt()


@sow.register
def _(arg: Seed):
    arg.grow()


pig = Pig()
seed = Seed()

sow(pig)
sow(seed)

