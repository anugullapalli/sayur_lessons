from functools import reduce

numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)

print(product)  # Output: 24

product = list(map(lambda x, y: x * y, numbers))
print(product)  # Output: 24
