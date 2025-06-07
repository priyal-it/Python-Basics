#Practical 117: Types of Exceptions
#Types of Errors: NameError, ZeroDivisionError, FileNotFoundError, IndexError, SyntaxError, TypeError, IndentationError
a=int(input("Enter Dividend: "))
b=int(input("Enter Divisor: "))
def div(x,y):
    return x/y

try:
    c=div(a,b)
    print(d)    #NameError: d not defined
    print(c)
    f=open('abc.txt','r')
except ZeroDivisionError:    #ZeroDivisionError if b==0
    print("Divisor cannot be Zero.")
except NameError:            #Variable d does not exist
    print("Variable not defined.")
except FileNotFoundError:   #abc.txt does not exist
    print("File does not exist.")
except IndexError:
    print("Invalid Index.")
finally:
    f.close()
    print("From finally block.")