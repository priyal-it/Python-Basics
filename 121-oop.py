#Practical 121: Attributes and Methods
class Student:
    def __init__(self, roll_no, name):
        self.roll_no=roll_no
        self.name=name
    def display(self):
        print(self.roll_no, self.name)

s0=Student(0,"Pratik")
s1=Student(1,"Prayag")
s0.display()
s1.display()