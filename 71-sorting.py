#lec 5.3: Sorting using Functions

def sort(l):
    m=[]
    while l:
        min_val=min(l)
        m.append(min_val)
        l.remove(min_val)
    return m
l=[6,45,21,3]

print(sort(l))