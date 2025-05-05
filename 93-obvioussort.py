#Find out the minimum most element in the list l
#Append that to a new list x
#Remove the minimum from the original list l
def obvious_sort(l):
    x=[]

    while l:
        min_val=min(l)
        x.append(min_val)
        l.remove(min_val)

    print(x)

l=input("Enter numbers separated by a space: ")
print(obvious_sort(l.split(" ")))