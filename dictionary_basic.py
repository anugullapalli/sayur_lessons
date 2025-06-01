# Creating a dictionary with student information
student = {
    "name": "Alice",
    "age": 20,
    "major": "Computer Science"
}
print(student)

# Accessing specific values
print(student["name"])  # Output: Alice

# Using get() to safely access a key
print(student.get("age"))  # Output: 20
print(student.get("grade", "Not Available"))  # Output: Not Available

# Adding a new key-value pair
student["grade"] = "A"

# Modifying an existing key-value pair
student["age"] = 21

print(student)
# Output: {'name': 'Alice', 'age': 21, 'major': 'Computer Science', 'grade': 'A'}
# Using pop() to remove a specific key-value pair
student.pop("grade")

# Using del to remove a key or clear() to empty the dictionary
del student["major"]
print(student)  # Output: {'name': 'Alice', 'age': 21}

student.clear()  # Clears all items
print(student)  # Output: {}

# Loop through keys
for key in student:
    print(key)

# Loop through values
for value in student.values():
    print(value)

# Loop through key-value pairs
for key, value in student.items():
    print(f"{key}: {value}")
