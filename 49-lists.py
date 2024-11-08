#warmup with lists

l=[1,4,5,7,8,100]

print(l)

l.append(1923)
l.append(32)
print(l)

l.remove(32)
l.remove(1923)
print(l)

l.append(2)
l.append(42)
l.append(2)
print(l)

l.remove(2)
print(l)

#list within a list
x=[]
x.append(l)
x.append(324)
print(x)

M=[]
M.append([1,2,3])
M.append([4,5,6])
M.append([7,8,9])

print(M)
print(M[0])
print(M[1])
print(M[2])
print(M[0][0])
print(M[0][1])
print(M[0][2])
#diagonal elements
print(M[0][0])
print(M[1][1])
print(M[2][2])
