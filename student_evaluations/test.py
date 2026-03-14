import re

def contains_at_least_one_letter(name):
    pattern = r'[a-zA-Z]'
    return bool(re.search(pattern, name))

# Test the function
print(contains_at_least_one_letter("John Doe"))  # True
print(contains_at_least_one_letter("123a4"))       # False
