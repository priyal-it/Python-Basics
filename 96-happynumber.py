#Write a python program to check whether a number is a happy number or not
def sumOfSquares(b):
    digits=len(str(b))
    squareSum=0
    for d in str(b):
        squareSum+=int(d)**2
    return squareSum
def isHappy(a):
    l=[]
    isUnhappy=True
    while isUnhappy:
        a=sumOfSquares(a)
        if a==1:
            isUnhappy=False
            return True
        elif a not in l:
            l.append(a)
        else:
            isUnhappy=True
            return False

n=int(input("Enter a number: "))
if isHappy(n):
    print(f"{n} is a happy number")
else:
    print(f"{n} is not a happy number")