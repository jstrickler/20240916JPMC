def trimmed(file_name):
    # function provides the body of the __next__() method
    with open(file_name) as file_in:
        for line in file_in:  # up to and including EOL  "\r"  or "\r\n"
            yield line.rstrip('\n\r')  # 'yield' causes this function to return a generator object
            # return in __next__()


mary_in = trimmed('../DATA/mary.txt')

print(f"{mary_in = }\n")

for trimmed_line in mary_in:
    print(trimmed_line)

with open('../DATA/mary.txt') as mary_in:
    contents = mary_in.read()
print(repr(contents))
