#obvious sort using two different functions

def min_val(l):
    min_val=l[0]
    for i in range(len(l)):
        if l[i]<min_val:
            min_val=l[i]
    return min_val

def obvious_sort(l):
    m=[]
    for i in range(len(l)):
        mini=min_val(l)
        m.append(mini)
        l.remove(mini)
    return m

p=[6,5,4,3]
p=obvious_sort(p)
print(p)