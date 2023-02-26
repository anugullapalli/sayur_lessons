
type="teacher"
if (type=="teacher"):
        print ("Hello teacher!")   #this one

type="student"
if (type=="teacher"):
        print ("Hello teacher!")
else:
        print ("Hello World!")     #this one

type="other"
if (type=="teacher"):
        print ("Hello teacher!")
elif (type=="student"):
        print ("Hello Student!")    
elif (type=="advisor"):
        print ("Hello Advisor!")  
else:
    print ("Hello World!")      #this one


    name=input("Enter your name")
    print ("Hello ",name)