
number_input = 1
while (number_input != 0):
    number_input= int(input ('Enter your number')) #get the number 

    if number_input == 0:
        continue
    if number_input > 0:
        print ("positive")
    else:
        print("negative")

