# numbers = []  # Create an empty list

# for i in range(5):  # Loop 5 times to collect input
#     num = int(input("Enter a number: "))
#     numbers.append(num)  # Append user input to the list

# print("Numbers entered:", numbers)

#sum all elements in the list
# numbers=[2,4,3,7,1,10]
# sum=0
# for num in numbers:
#     sum+= num

# print ('sum is: ', sum)

# even_numbers=[]
# num = 2
# sum = 0
# while (sum <= 20):
#     even_numbers.append(num)
#     sum += num
#     num += 2

# print("Even Numbers entered:", even_numbers)

# words = ["apple", "banana", "cherry", "apple", "banana", "apple"]

# count = 0

# for word in words:
#     if word == 'apple':
#         count +=1

# print('count is: ',count)

numbers = [12, 45, 23, 67, 34] 

min = numbers[0]

for i in numbers:
    
    if i< min:
        min = i

print('min is', min)
 
numbers = [-12, -45, -23, -67, -34] 

max = numbers[0]

for i in numbers:
    
    if i> max:
        max = i

print('max is', max)
 