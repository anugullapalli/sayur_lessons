greet = lambda : print('Hello world')
greet()


greet_user = lambda name: print('Hello', name)
greet_user('Anu')


def double(n):
   return 2*n

def triple(n):
   return 3*n

def myfunc(n):
   return lambda a: a * n 
## a Unknown number

mydoubler = myfunc(2)
mytripler = myfunc(3)

print (double(7))
print (mydoubler(7))

print (triple(7))
print (mytripler(7))
