
class animal:
    def eat(self):
            print ("I can eat!")
    def sleep(self):
            print ("I can sleep")
    def make_sound(self):
            print("I can make sounds")

#derived class
class dog(animal):
    def make_sound(self):
            print("I make woof woof sounds")

class cat(animal):
    def make_sound(self):
          print("I can make meow meow sounds")

#create dog object
dog1=dog()
dog1.eat()
dog1.sleep()
dog1.make_sound()

cat1=cat()
cat1.eat()
cat1.sleep()
cat1.make_sound()

rabbit1=animal()
rabbit1.eat()
rabbit1.sleep()
rabbit1.make_sound()

#