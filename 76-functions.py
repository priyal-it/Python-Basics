#lec 5.8: Write a Python code using functions to calculate area and perimeter of circle and rectangle

def area_circle(r):
    return 3.14*r**2

def peri_circle(r):
    return 2*3.14*r

def area_rect(l,b):
    return l*b

def peri_rect(l,b):
    return 2*(l+b)

r=7
l=5
b=6

print(f'The area of a circle with radius {r} is {area_circle(r)}')
print(f'The circumference of a circle with radius {r} is {peri_circle(r)}')
print(f'The area of a rectangle with length {l} and breadth {b} is {area_rect(l,b)}')
print(f'The perimeter of a rectangle with length P{l} and breadth {b} is {peri_rect(l,b)}')