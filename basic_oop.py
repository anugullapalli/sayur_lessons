class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says Woof!")

    def use(self):
        print(f"{self.name} can be your protector!")
    

# Create an object
dog = Dog("Buddy", "Golden Retriever")
dog.bark()
dog.use()

dog2 = Dog("Tommy","German Shepherd")
dog2.use()
