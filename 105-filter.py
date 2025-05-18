#Practical 105: Filter Function
import math
lst=[1,-5,100,4,-8]

square_root=lambda n: math.sqrt(n)

def is_positive(n):
    if n>=0:
        return n

print(list(map(square_root,filter(is_positive,lst))))