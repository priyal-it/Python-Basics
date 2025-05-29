#Practical 114: Search using Recursion
def obvious_search(l,a):
    '''check if a given element a is present in a list l or not.'''
    for x in l:
        found=False
        if x==a:
            print('The number was found.')
            return True
            break
    print('The number was not found.')
    return False
