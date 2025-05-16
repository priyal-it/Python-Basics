#104 Map Function
a=[10,20,30]
b=[1,2,3]
add=lambda x,y:x+y
print(list(map(add,a,b)))

add1=lambda x:x+1
print(list(map(add1,a)))