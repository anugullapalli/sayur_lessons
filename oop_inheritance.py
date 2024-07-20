class bird:
    name = ""
    age = 0

#derived class
class parrot(bird):
    fly_height = 100
    color="green"

class eagle(bird):
    eyes = "black"

#create parrot object
parrot1 = parrot()
parrot1.name = "blu"
parrot1.age = 10

parrot2 = parrot()
parrot2.name = "red"
parrot2.age = 8

eagle1=eagle()
eagle1.name="raja"
eagle1.age=20

print(f"{parrot1.name} is {parrot1.age} years old and flying height is {parrot1.fly_height}")
print(f"{parrot2.name} is {parrot2.age} years old and flying height is {parrot2.fly_height}")
print(f"{eagle1.name} is {eagle1.age} years old and color of eyes is {eagle1.eyes}")