#Problem 1: Finding the factorial with error handling
n=int(input("Enter a number: "))
fact=1

if(n>=0):
    while(n>0):
        fact=fact*n
        n-=1

    print(fact)
    
else:
    print("Not defined")