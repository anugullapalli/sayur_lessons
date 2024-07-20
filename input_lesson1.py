name = "Anu"
print("Your name is:", name)

# Suppose,  there are three students, first student brought Rs.1000 and second student brought 800 and 
# another structure brough 1200. They went spent 2000 at weekend outing. 
# They have 1000 amount is pending and we want to distribute back to the students. 
# 1.How do you want to distribute them ? 
# write short progam to express your idea through python program
# How to apply same logic, Suppose 10 students and each student brought 500.
# through this homework, we are exploring  basic variables and operations and input and output operations. 
student_count = 3
student1_amount = 1000
student2_amount=800
student3_amount=1200
total_amount = student1_amount + student2_amount + student3_amount
print("Your total is:", total_amount)

spent_amount=2000
total_amount = total_amount - spent_amount
print("Your total remaining is:", total_amount)

distribute_amount = total_amount /student_count
print("Distribute amount is:", round(distribute_amount,2))

student_count = 10
student_amount = 500
total_amount = student_amount * student_count
print("Your total is:", total_amount)

spent_amount=2000
total_amount = total_amount - spent_amount
print("Your total remaining is:", total_amount)

distribute_amount = total_amount /student_count
print("Distribute amount is:", round(distribute_amount,2))
