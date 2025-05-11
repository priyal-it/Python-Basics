#Problem 2: Write a python code using functions to calculate area and perimeter of circle and rectangle
def areaOfRectangle(l,b):
    return l*b

def areaOfCircle(r):
    return 3.14*r**2

def perimeterOfRectangle(l,b):
    return 2*(l+b)

def circumferenceOfCircle(r):
    return 3.14*r

l=float(input("Enter length of Rectangle: "))
b=float(input("Enter breadth of Rectangle: "))
r=float(input("Enter radius of Circle: "))

print(f"Area of Rectangle is: {areaOfRectangle(l,b)}")
print(f"Perimeter of Rectangle is: {perimeterOfRectangle(l,b)}")
print(f"Area of Circle: {areaOfCircle(r)}")
print(f"Circumference of Circle: {circumferenceOfCircle(r)}")