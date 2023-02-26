userstring=input("Enter input string: ")
print (userstring)


print (userstring[0])
print (len(userstring))
ind = 0
for i in range(0,len(userstring) - 1):
        if userstring[i] =='a':
                ind = i
                print (i + 1)
print (ind)