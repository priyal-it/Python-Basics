#Practical 121: Inheritance and Method Overriding
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(self.name,self.age)

class Student(Person):
    def __init__(self,name,age,marks):
        super().__init__(name,age)
        self.marks=marks
    def display(self):
        super().display()
        print(self.marks)

class Employee(Person):
    def __init__(self,name,age,salary):
        super().__init__(name,age)
        self.salary=salary
    def display(self):
        super().display()
        print(self.salary)

s0=Student("Shiksha",18,150)
s0.display()
e0=Employee("Parth",18,50000)
e0.display()