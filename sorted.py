# numbers = [3,6,2,1,5]

# sorted_numbers = sorted(numbers)
# print (sorted_numbers)

# sorted_numbers=sorted(numbers, reverse=True)
# print (sorted_numbers)

# top_3 = sorted_numbers[0:3]
# print (top_3)

fruit =["apple","mango","orange", "grapes","watermelon","strawberry"]
sales = [100,50,200,30,20,150]

fruitList = list(enumerate(fruit))
print(fruitList)

salesList = list(enumerate(sales))
print(salesList)

# sortedSales = sorted(salesList)
# print (sortedSales)

# sortedSales = sorted(salesList,reverse=True)
# print (sortedSales)


sortedSales = sorted(salesList,key=lambda x:x[1],reverse=True)
print (sortedSales)

top_3 = sortedSales[0:3]
print (top_3)

