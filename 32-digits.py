#Problem 2: Find the number of digits in a given number using while loop

n=int(input("Enter a number: "))

digits=1
if(n>=10):
    while(n>9):
        n=n/10
        digits+=1

print(digits)