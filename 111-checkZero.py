#Practical 111: Check Whether 0 is Present in a List or Not
def checkzero(l):
    if len(l)==0:
        return False
    elif l[0]==0:
        return True
    else:
        l=l[1::]
        return checkzero(l)

print(checkzero([121,234,0]))