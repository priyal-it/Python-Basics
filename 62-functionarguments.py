#lec 4.10: Types of function arguments

def add(c,a,b):     #function definition
    return (a+b-c)  #return statement

print(add(10,20,20)) #add(a,b,c) function call

#(10,20,20) (VALUES) function arguments
#(a,b,c) (VARIABLES) function parameters

print(add(a=10,b=20,c=20))

#no. of arguments should be equal to no. of parameters

#def add(a=10,b=20,c=20) #default arguments
# print(add(a=10,b=20,c=20)) #keyword arguments
