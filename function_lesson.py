#PYTHON functions

#block of code you want to run when it is called
# pass parameters (arguments, values)
# can return a result
#define function


def hello_function2(*names):
    print("hello" + names[0]+ names[1])

#invoke/call function
hello_function2("anu","chitra","student")

def hello_fn3(fname, lname):
    print("hello" + fname +  lname)

hello_fn3("anu","gullapalli")
hello_fn3 (lname="gullapalli", fname="anu")
#default value - only if the value is not present
def hello_fn4(fname="teacher", lname="student"):
   print("hello" + fname +  lname)

hello_fn4("anu","radha")     # hello anu radha
hello_fn4()                  # hello teacher student
hello_fn4("anu")             # hello anu student
hello_fn4(lname="radha")     # hello teacher radha


#recursive function
# get input number n
# 5
# 1+2+3+4+5  = total
# 4
# 1+2+3+4
#3
# 1+2+3
# 2
#1+2
def sum_recursion(n):
    if (n > 0):
        result= n + sum_recursion(n-1)
    else:
        result = 0
    return result

print (sum_recursion(4))

