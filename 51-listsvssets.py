#lec 4.2 Lists and sets

#lists
l=list(range(10))
print(l)

l.append("Patel")
l.append("India")
print(l)

print('India' in l)

print(-1 in l)
print("Patel" in l)
print("IndiA" in l)

m=list(range(100))
print(m[len(m)-1])
print("Patel" in m)

print(0 in m)
print("India" in m)
print(m[0])

#sets
y={1,7,6,2,4,8,1}
print("Y = ",y)
print(2 in y,10 in y)
print(type(y))
print(type(m))
''' 
#list takes lesser time to create than set when creating in a large range
#while searching for an element in a numeric list or a set, set is a quicket option

criteria                            list                set
searching                           disadvantage        advantage
accessing an element using index    advantage           disadvantage
'''