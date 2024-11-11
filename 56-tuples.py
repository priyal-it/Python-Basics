#lec 4.6 More on Tuples

#indexing, slicing, iteration is possible with tuples
t={1,2,3}
print(t,type(t))

x,y,z=t
print(x,y,z)

a=5
b=20
a,b=b,a
print(a,b)

l=[10]
print(l,type(l))

m=(10)
print(t,type(t))
n=(10,)
print(t,type(n))

o=([1,2],['a','b'])
print(o,type(o))
o[0][0]=10
print(o,type(o))

t1=(1,2,3)      #hashable
t2={[1,2,3],}   #not hashable
