#Find out the minimum most element in the list l
#Append that to a new list x
#Remove the minimum from the original list l

l=[6,4,1,7,5,2,3]
x=[]

while l:
    min_val=min(l)
    x.append(min_val)
    l.remove(min_val)

print(x)