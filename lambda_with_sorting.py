# Sort students by age
sorted_students = sorted([1,5,2,3])

print(sorted_students)

students = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 20},
    {'name': 'Charlie', 'age': 23}
]

# Sort students by age
sorted_students = sorted(students, key=lambda student: student['name'])

print(sorted_students)
# Output: [{'name': 'Bob', 'age': 20}, {'name': 'Charlie', 'age': 23}, {'name': 'Alice', 'age': 25}]

