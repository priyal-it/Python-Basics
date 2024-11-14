#lec 4.9 More examples of functions

#finding the minimum element in a list using function

def listMin(l):
    m=l[0]
    for i in range(len(l)):
        if l[i]<m:
            m=l[i]
    return m

l=[3,5,6,7,8]
print(listMin(l))

def listMax(l):
    m=l[0]
    for i in range(len(l)):
        if l[i]>m:
            m=l[i]
    return m

print(listMax(l))

def list_appendbefore(l,z):
    newl=[]
    for i in range(len(l)):
        newl.append(l[i])
    for i in range(len(l)):
        newl.append(z[i])    

    return newl

l=[1,2,3]
z=[10,20,30]
print(list_appendbefore(l,z))

def list_avg(l):
    sum=0
    j=0
    for i in range(len(l)):
        sum=sum+l[i]
        j+=1
    avg=sum/j
    return avg

print(list_avg(l))