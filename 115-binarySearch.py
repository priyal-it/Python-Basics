#Practical 115: Binary Search
def binary_search(l,a):
    low=0
    high=len(l)-1

    while(low<=high):
        mid=(low+high)//2
        if l[mid]==a:
            print("The number was found.")
            return True
        elif l[mid]<a:
            low=mid+1
        else:
            high=mid-1
    print("The number was not found.")
    return False