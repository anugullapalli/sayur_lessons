students = {'Alice': 85, 'Xavier': 70, 'Charlie': 25}

# Find the student with the highest score
top_student = max(students.items(), key=lambda item: item[1])
print(top_student)  
