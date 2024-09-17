#

strings = ['wombat', 'koala', 'kookaburra', 'blue-ringed octopus']

result = [s.upper() for s in strings]  # Using a list comprehension, which is usually simpler than map()
print(result, "\n")

#   map(lambda s: s[:3], strings)
result = map(str.upper, strings)  # Using map to copy list to upper case
print(result)
print(list(result), "\n")

result = map(len, strings)  # Using map to get list of string lengths
print(result, "\n")
for length in result:
    print(length)
