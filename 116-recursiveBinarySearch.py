#Practical 116: Binary Search Using Recursion
def recursive_binary_search(l,a,low,high):
    if low>high:
        print("The number was not found.")
        return False
    
    mid=(low+high)//2

    if l[mid]==a:
        print("The number was found.")
        return True
    elif l[mid]<a:
        return recursive_binary_search(l,a,mid+1,high)
    else:
        return recursive_binary_search(l,a,low,mid-1)