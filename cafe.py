import re


class Menu_Item:
    # constructor
    def __init__(self, name, price, stock, sales, profit):
        # data members
        self.name = name
        self.price = price
        self.stock = stock
        self.sales = sales
        self.profit = profit
    # method
    # to display employee's details
    def show(self):
        # accessing public data member
        print("Name: ", self.name, 'Price:', self.price)
    # method
    def update_qty(self,customer_qty):
        self.stock -= customer_qty
        print("Name: ", self.name, 'Current Quantity:', self.stock)

class drink_Menu_Item(Menu_Item):
    def update_qty(self,customer_qty):
        self.stock -= customer_qty
        if (self.stock < 100):
            print("Time to reorder")
        print("Name: ", self.name, 'Current Quantity:', self.stock)  

vadai= Menu_Item("vadai",10,50,0,4)
tea=drink_Menu_Item("tea",12,45,0,5)
coffee=drink_Menu_Item("coffee",15,40,0,6)

vadai.show()
vadai.update_qty(2)
tea.update_qty(2)

# customer_input = []
# for customers in range(1) :
#     order = input("enter your order: ")
#     quantity = re.findall(r'\b(\d{2}|\d+)\b' , order)
#     items = re.findall(r'\b(vadai|tea|coffee)\b',order.lower())
#     print (items)
#     print (quantity)
   
#     """  if item == "vadai" :
#             x = menu.index("vadai")
#             qty= int(quantity[index])
#             if qty < stock[x] :
#                 stock[x] -= qty
#                 sales[x] += qty
#             else :
#                 print(f"only {stock[x]}vadai is available :" )
#         elif item == "tea" :
#             x = menu.index("tea")
#             qty= int(quantity[index])
#             if qty < stock[x] :
#                 stock[x] -= qty
#                 sales[x] += qty
#             else :
#                 print(f"only {stock[x]} tea is available :" )
#         else :
#             x = menu.index("coffee")
#             qty= int(quantity[index])
#             if qty < stock[x] :
#                 stock[x] -= qty
#                 sales[x] += qty
#             else :
#                 print(f"only {stock[x]}coffee is available :" ) """
#     for index,item in enumerate(items) :
#         x = menu.index(item)
#         qty= int(quantity[index])
#         if qty < stock[x] :
#                 stock[x] -= qty
#                 sales[x] += qty
#         else :
#                 print(f"only {stock[x]}vadai is available :" )
# for index, sale in enumerate (sales) :
#     final_profit = sales [index] * profit [index]
#     print(f"profit for {menu[index]} is {final_profit}")