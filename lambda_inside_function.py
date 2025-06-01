def make_multiplier(factor):
    return lambda x: x * factor

# Create a function to double a number
double = make_multiplier(3)

print(double(10))  # Output: 10
