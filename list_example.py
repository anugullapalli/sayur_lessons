item_list = ["apple","banana","orange"]
inventory_list = [20,30,10]
min_count_list = [5,10,3]
reorder_count_list = [10,20,5]

# def reorder_item(item_name, sale_count):
#          print (item_list[0])
#          print (len(item_list))
#          for i in range (0,len(item_list)):
#             if (item_name == item_list[i]):
#                 return i
        
# fruit_index = reorder_item("apple",5)
# print (fruit_index)
# inventory_list[fruit_index] -= 5
# print(inventory_list.keys())

# carDict = {
#     "brand" : "Toyota",
#     "model" : "Corolla",
#     "year" : 1995
# }
# item_list = ["apple","banana","orange"]
# inventory_list = [20,30,10]
# min_count_list = [5,10,3]
# reorder_count_list = [10,20,5]

myDict = {
    "apple" : {
        "Inventory" : 20,
        "MinCount" : 5,
        "ReCount" : 10
    },
    "banana" : {
        "Inventory" : 30,
        "MinCount" : 10,
        "ReCount" : 20
    },
    "orange" : {
        "Inventory" : 10,
        "MinCount" : 3,
        "ReCount" : 5
    }
}
print(myDict["apple"]["Inventory"])