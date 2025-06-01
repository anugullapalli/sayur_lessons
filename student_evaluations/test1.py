# Write a program that prints numbers from 1 to 100.
# if that number is divisible by 2 , print "Sayur Rocks!"
# If that number is divisible by 4, print "Sayur Really Rocks!!"

#logic
# i = 1 limit 100
# for loop to loop through numbers
# if i is divisible by 2 , print sayur rocks
# else if i is divisible by 4, print sayur really rocks
# print i
#

for i in range (1,11):
    

    if (i % 4 == 0):
        print ("Sayur Really Rocks!")
        print("Sayur Rocks!")
    elif (i % 2 ==0):
        print("Sayur Rocks!!")
    else:
       print(i)
