 
myname="Anu"    #define a variable and assinged a value  #global

print (myname)     #global variable  #1

def test_scope(name):
    print(name)   #passed parameter
    message="Happy Birthday"   #variable scope within that function
    print (message, name)

test_scope(myname)
print(myname)           #global
print (message, myname)