#lec 04: Variables, Operators and Expressions
roll=1
Roll=2
print(roll,Roll)
#variables in python are case sensitive

x=y=z=10

print(x,y,z)

#swapping variable values
a=1
b=2
print(a,b)
a,b=b,a
print(a,b)

#deleting a variable
x=10
print(x)
del(x)

#shorthand operators
#addition
count=0
count=count+1
count=count+1
count=count+1
count=count+1
print(count)

del(count)

count=0
count+=1
count+=1
count+=1
count+=1
print(count)

del(count)

#subtraction
count=10
count-=1 #used shorthand operator
count=count-1
print(count)

del(count)

#division
count=10
count/=2
count/=5
print(count)

#expressions
x=5
print(1<x<10)
print(10<x<20)
print(x<10<x*10<100)
print(10>x<=9)
print(5==x>4)