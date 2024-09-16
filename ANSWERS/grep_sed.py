import typing as T


def grep(x: str) -> T.Generator[str, str, None]:
    """Only emits lines of text that contain x"""
    coll = ""
    while True:
        coll = yield coll if x in coll else "Not Found"


def sed(pattern: str, replacement: str):
    """Replace any lines containing pattern with replacement"""
    value = ""
    while True:
        value = yield value.replace(pattern, replacement)


with open('../DATA/mary.txt') as mary_in:
    lines = [line.rstrip() for line in mary_in]
print(lines)

g = grep('lamb')
next(g)

for line in lines:
    print(g.send(line))
print('-' * 60)

s = sed('lamb', 'wombat')

next(s)
for line in lines:
    print(s.send(line))
print()

s = sed('Mary', 'Oscar')
next(s)
for line in lines:
    print(s.send(line))
