# get the input "enter the number (to end enter 0)"
# If the number is negative, print negative
# else print positive
# enter the number (to end 0) 1
# number is positive
# enter the number (to end 0) 2
# number is event
# enter the number (to end 0) 0 
# end the while loop

number = 10
while (number != 0): 
    print ("number is " , number)                                      #while loop block start
    number=int(input("Enter the number (to end enter 0): "))
    if number == -1: continue                         #skip rest of the block
    if number == -2: break                            #skips entire loop
    if (number > 0):
        print ("number is positive")
    else:
        print("number is negative")                        #while loop block end

print("end of block")
print("end")

