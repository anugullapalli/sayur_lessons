#sample program to write hello world
#comments line2
#comments line3

#print("Hello World!")   #first print statement

##name=input("Enter your name")    #syntax errors  (typos, missing quotes , etc.,)
#print(1/0)      #run time errors
#print ("1+1=3")   #logical errors

my_str = 'Hello Sayur'      #string data type
my_num = 10                 #integer data type
my_float = 10.5             #float data type

grade_mark = int(input("Enter your grade mark"))

if grade_mark >= 90:
    print ("distinction")
elif grade_mark >= 80:
    print ("first class")
elif grade_mark >= 70:
    print("second class")
else :   
    print("pass")
