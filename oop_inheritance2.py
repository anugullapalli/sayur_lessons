class animal:
    def eat(self):
            print ("I can eat!")
    def sleep(self):
            print ("I can sleep")

#derived class
class dog(animal):
    def bark(self):
            print("I can bark!")
    def eat(self):
            print ("I can eat bones!")

class cat(animal):
    def night_vision(self):
          print("I can see in the dark")

#create dog object
dog1=dog()
dog1.eat()
dog1.sleep()
dog1.bark()

cat1=cat()
cat1.eat()
cat1.sleep()
cat1.night_vision()

rabbit1=animal()
rabbit1.eat()
rabbit1.sleep()
