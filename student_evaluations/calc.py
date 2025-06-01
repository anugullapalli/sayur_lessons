#Fill in the missing code whereever it says #FillinMissingCode
#Fix the syntax errors as needed.

#This is code has functions for basic arithmetic operations. Add, subtract, multiply and divide
#The main function adds all student marks and finds the average

def addTwoNumbers(n1, n2):
    ans = n1 + n2
    return ans
def subtractAfromB(a, b):
    ans = b-a
    return ans
def multiplyTwoNumbers(n1,n2):
    ans = n1 * n2
    return ans


def divideAFromB(a,b):
    ans = b/a
    return ans

#main code

def list_total(lst):
    total = 0
    for i in lst:
        total = addTwoNumbers(total,i)
    return total


print(list_total([1,2,3]))

print(list_total([3,4,5,6,7,8]))


marksInMaths = [56,78,56,45,90]
total = list_total(marksInMaths)
mathAvg = divideAFromB(5,total)
#FillinMissingCode to calculate avg for Maths

marksInScience = [90,78,67,8,98]
total = list_total(marksInScience)
scienceAvg = divideAFromB(5,total)
#FillinMissingCode to calculate avg for Maths


marksInHistory = [87,44,56,34,90]
total= list_total(marksInHistory)
historyAvg = divideAFromB(5,total)
#FillinMissingCode to calculate avg for History


total= list_total([mathAvg,scienceAvg,historyAvg])

#total=addTwoNumbers(mathAvg,scienceAvg)
#total=addTwoNumbers(total,historyAvg)

totalAvg = divideAFromB(3, total)
#Call divide function to get the average from all three subjects
#FillinMissingCode

print("The avg mark is ", totalAvg)