#Practical 118: Handling ZeroDivisionError
div = lambda x,y: x/y
a=int(input("Enter the Dividend: "))
b=int(input("Enter the Divisor: "))
try:
    c=div(a,b)
    print(div(a,b))
except ZeroDivisionError:
    print("Divisor Cannot be Zero")