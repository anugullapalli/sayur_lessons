#sample program to write hello world
#comments line2
#comments line3

#print("Hello World!")   #first print statement

##name=input("Enter your name")    #syntax errors  (typos, missing quotes , etc.,)
#print(1/0)      #run time errors
#print ("1+1=3")   #logical errors

#get 3 subject marks are input and then print the grade


my_str = 'Hello Sayur'      #string data type
my_num = 10                 #integer data type
my_float = 10.5             #float data type

mark1 = int(input("Enter your subject 1 mark:"))
mark2 = int(input("Enter your subject 2 mark:"))
mark3 = int(input("Enter your subject 3 mark:"))

grade_mark = (mark1 + mark2 + mark3)/3   #calculating the average

print ("Your grade mark is", grade_mark)

if grade_mark >= 90:
    print ("Your grade is distinction")
elif grade_mark >= 80:
    print ("You grade is first class")
elif grade_mark >= 70:
    print("Your grade is second class")
else :   
    print("Your grade is pass")
