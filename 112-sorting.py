#Practical 112: Sorting Recursively
def mini(l):
    x=l[0]
    for i in range (len(l)):
        if x>l[i]:
            x=l[i]
    return x

def sort(l):
    if len(l)<=1:
        return l
    m=mini(l)
    l.remove(m)
    return [m]+sort(l)

l=[21,3,56,45]
print(sort(l))