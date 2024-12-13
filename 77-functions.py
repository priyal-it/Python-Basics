#lec 5.8: Write a Python code using functions to calculate area and perimeter of circle and rectangle
#getting inputs from user

def area_circle(r):
    return 3.14*r**2

def peri_circle(r):
    return 2*3.14*r

def area_rect(l,b):
    return l*b

def peri_rect(l,b):
    return 2*(l+b)

polygon=1
while (polygon!='0'):
    print("\n\nEnter Polygon Shape\n\n1 for circle\n2 for rectangle")
    polygon=int(input("Enter 1 or 2 (0 to terminate): "))
    
    if polygon == 1:
        r=int(input("Enter radius of circle: "))
        print(f'The area of a circle with radius {r} is {area_circle(r)}')
        print(f'The circumference of a circle with radius {r} is {peri_circle(r)}')

    if polygon == 2:
        l=int(input("Enter length of the rectangle: "))
        b=int(input("Enter breadth of the rectangle: "))
        print(f'The area of a rectangle with length {l} and breadth {b} is {area_rect(l,b)}')
        print(f'The perimeter of a rectangle with length {l} and breadth {b} is {peri_rect(l,b)}')

    if polygon == 0:
        print("Loop terminated.")
        break
