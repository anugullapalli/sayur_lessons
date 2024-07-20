class Employee:
    def __init__(self,name):
        self.name = name
        self.mgr=self

    def print(self):
        print("Name: {}".format(self.name))
        print("Manager: {}".format(self.mgr.name))


e1 = Employee("anu")
e2= Employee("chitra")
e1.name = "Lalitha"
e1.mgr=e2
print(e1.name)
e1.print()



class Person:

    def __init__(self, name):
       self.__name = name

    def print(self):
        print("Name: {}".format(self.__name))
       

a= Person("Krishna")
a.name = "Lalitha"
a.print()


class Employee:
    # constructor
    def __init__(self, name, salary, project):
        # data members
        self.name = name
        self.salary = salary
        self.project = project

    # method
    # to display employee's details
    def show(self):
        # accessing public data member
        print("Name: ", self.name, 'Salary:', self.salary)

    # method
    def work(self):
        print(self.name, 'is working on', self.project)

# creating object of a class
emp = Employee('Jessa', 8000, 'NLP')

# calling public method of the class
emp.show()
emp.work()