def calculate_area(length, width):
    global rectangle_area 
    rectangle_area = length * width
  

# Calling the function with multiple parameters
length = 10
width = 5
calculate_area(length, width)

print(f"The area of the rectangle is: {rectangle_area}")



#length = 10, width = 5 (global)
#rectangle_area (50) = calculate_area(10,5) = return vLUE OF 50
#length = 10, width = 5(local)
#area = 50 (local)
# all lcoal erased

