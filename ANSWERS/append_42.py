def append_42(alist: list = None) -> list:
    if alist is None:
        alist = []
    alist.append(42)

    return alist

data = [1, 2, 3]
result = append_42(data)
print(data)
print(result)

result = append_42()
print(result)


