#Practical 120: Classes and Objects

#Creating a class
class Student:
    roll_no=None
    name=None

#Creating Objects and accessing its values
s0=Student()
s0.roll_no=0
s0.name="Priyal"
print(s0.roll_no,s0.name)

s1=Student()
print(s1.roll_no, s1.name)

s2=Student()
s2.roll_no=2
s2.name="Ashwin"
print(s2.roll_no, s2.name)

s50=Student()
s50.name="Asmita"
print(s50.roll_no, s50.name)