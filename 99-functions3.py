#Problem 3: Write a python code using functions which checks whether the input coordinates form a triangle or not
def isTriangle(a,b,c):
    if (1/2)*(int(a[0])*(int(b[1])-int(c[1]))+int(b[0])*(int(c[1])-int(a[1]))+int(c[0])*(int(a[1])-int(b[1])))!=0:
        return True
    else:
        return False

a=input("Enter First Coordinate separated by a space: ").split(" ")
b=input("Enter Second Coordinate separated by a space: ").split(" ")
c=input("Enter Third Coordinate separated by a space: ").split(" ")

if isTriangle(a,b,c):
    print("It is a Triangle")
else:
    print("It is not a Triangle")
