students = {
    "Alice": {"Math": 85, "English": 78},
    "Bob": {"Math": 90, "English": 80},
    "Charlie": {"Math": 70, "English": 65}
}

students["Alice"]["Science"]=88
students["Bob"]["Science"]=78
students["Charlie"]["Science"]=65

print(students)

# Calculate average score for each student
for student, subjects in students.items():
    avg_score = sum(subjects.values()) / len(subjects)
    print(f"{student}'s average score: {avg_score:.2f}")

