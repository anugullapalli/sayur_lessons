numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#even_numbers = list(map(lambda x: x % 2 == 0, numbers))

#print(even_numbers) 

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(even_numbers)  # Output: [2, 4, 6, 8]