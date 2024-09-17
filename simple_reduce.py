from operator import add, mul
from functools import reduce


nums = [800, 80, 1000, 32, -3, 8, 18, 255, 400, 5, 5000]

total = reduce(add, nums)
print(f"{total = }")

#   (((800 + 90) + 1000) + 32) ...

product = reduce(mul, nums)
print(f"{product = :,d}")


