#lec 3.4 More on Lists

#operators

#addition '='
l1=[1,2,3]
l2=[10,20,30]
l12=l1+l2
l21=l2+l1
print(l12,l21)

#repetition '*'
l1=[1,2,3]*3
print(l1)

#Equality '=='
l1=[1,2,3]
l2=[1,2,3]
l3=[1,3,2]
print(l1==l2)
print(l1==l3)
print(l1<=l2)
print(l1<=l3)

l=[1,2,4]
print(l)
l[2]=3
print(l)

'''
s="abce"
print(s[3])
print(s[3])
s[3]='d'
print(s)

#throws an error, string is not mutable but lists are
'''

x=5
y=x
x=10
print(x,y)

l1=[1,2,3]
l2=l1 #stores the memory location and adds a new name to the same memory
l1[0]=100
print(l1,l2)

#ways to create a new memory location to avoid future changes to a copied list
l1=[1,2,3]
l2=list(l1)
l3=l1[:]
l4=l1.copy()
l5=l1
print(l1 is l2)
print(l1 is l3)
print(l1 is l4)
print(l1 is l5)

def add(x):
    x=x+1
    return x

x=5
print(add(x))
print(x)

l=[1,2,3]
print(l)
l.append(4)
print(l)
l.insert(2,9)
print(l)
l.pop(0) #removes element at i th position (pop(i))
print(l)
l=[23,3,5,6,754]
l.sort(reverse=True)
print(l)
l.reverse()
print(l)