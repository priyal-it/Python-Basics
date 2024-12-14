#lec 5.8: Write a Python code using functions which checks whether the input coordinates form a triangle or not

'''
When is a triangle, a triangle.
--> When the points/coordinates are not collinear.

When are the points/coordinates collinear?
--> When area of the triangle is zero.
--> They form a single straight line. If they do, then the sum of distance between any two distances is equal to the third distance.

d1+d2=d3
d1+d3=d2
d2+d3=d1
'''

def dist(A,B):
    import math
    A[0]=int(A[0])
    A[1]=int(A[1])
    B[0]=int(B[0])
    B[1]=int(B[1])
    return math.sqrt((B[0]-A[0])**2+(B[1]-A[1])**2)

def isTriangle(A,B,C):
    d1=dist(A,B)
    d2=dist(B,C)
    d3=dist(A,C)

    if (d1+d2==d3) or (d2+d3==d1) or (d1+d3==d2):
        return 1
    else:
        return 0

#taking input of the points.

print("Enter the coordinates: ")

a=input("Enter the first coordinate: ")
b=input("Enter the second coordinate: ")
c=input("Enter the third coordinate: ")

A=a.split(",")
B=b.split(",")
C=c.split(",")

if(isTriangle(A,B,C)):
    print("It is not a Triangle.")
else:
    print("It is a triangle.")
"""
Calculating the distance

d=sqrt((x2-x1)**2+(y2-y1)**2)

"""

