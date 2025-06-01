#Fill in the missing code whereever it says #FillinMissingCode
#Fix the syntax errors as needed.

#This is code has functions for basic arithmetic operations. Add, subtract, multiply and divide
#The main function adds all student marks and finds the average

def addTwoNumbers(n1, n2):
    ans = n1 + n2
    return ans
def subtractAfromB(a, b):
    sub=b-a
    return sub

def multiplyTwoNumbers(n1,n2):
    mul=n1 * n2
    return mul
def divideAFromB(a, b):
    ans = b / a
    return ans
#main code

#Get 5 marks from student and find the total
total = 0
mark_list=[]
for i in range(0,5):
    mark = int(input(f"Enter mark {i+1} "))
    mark_list.append(mark)

total = addTwoNumbers(mark_list[0],mark_list[1])
total = addTwoNumbers(total,mark_list[2])
total = addTwoNumbers(total,mark_list[3])
total = addTwoNumbers(total,mark_list[4])

avg = divideAFromB(5,total)

print("The avg mark is ", avg)