def greet(name):
    print ('Hello', name, "from Sayur")
#greet("Anu")

#greet = lambda : print('Hello world')
#greet()


greet_user = lambda company: print('Hello',  company)

google_greet_user= greet_user('from google')
#google_greet_user()

sayur_greet_user= greet_user("from sayur")
#sayur_greet_user()




def double(n):
   print (2*n)
#double(7)
def triple(n):
    print (3*n)
#triple(7)

def myfunc(n):
    return lambda a: a * n 
# ## a Unknown number

mydoubler = myfunc(2)
mytripler = myfunc(3)
myquadruple = myfunc(4)

#print (double(7))
print (mydoubler(7))

# print (triple(7))
print (mytripler(7))
print (myquadruple(7))

def tipfunc(n):
    return lambda amt: amt * n/100

tiptenpercent = tipfunc(10)
tipfifteenpercent = tipfunc(15)
tiptwentypercent = tipfunc(20)

print(tiptenpercent(250))
print(tipfifteenpercent(250))
print(tiptwentypercent(250))


    

upper = lambda string: string.upper()
print (upper("mango"))   

#given a number, i want to add 1
a=15

#print((lambda x: x[:3])(a))

print ((lambda x: "Double digit" if (x>=10) else "Single digit")(a))


print ((lambda x: x*10 if x>10 else (x*5 if x<5 else x))(11))

list = [33,44,5,1,11]
newlist= tuple(filter(lambda x: x>10, list))
print (newlist)

a=10
b=12
result = lambda x,y:x+y
print(result(a,b))
result2= lambda n:n+10
print(result2(9))