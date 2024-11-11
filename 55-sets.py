#lec 3.5 More on sets

st={1,2,4,3,5,1,2,3,4} #indexing is not possible in sets
print(st)

#subset
A= {1,4,6}
B={1,3,5,6}
C={1,3,4,6}
D={1,3,4,5,6}
print(A.issubset(C))
print(B.issubset(C))

#superset
print(C.issuperset(A))
print(C.issuperset(B))

#intersection and subtraction
S={1,2,3}
T={3,4,5}
C1=S.intersection(T)
C2=T.intersection(S)
C3=S-T
print(C1,C2,C3)