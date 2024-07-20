# Python code to illustrate read() mode
# r - read mode, w- for write mode, a- append
# file = open("example1.txt", "a") 
# file.write("did not delete the previous line")
# file.close()

file = open("emp_data.json", "r") 

for each in file:
   print (each)