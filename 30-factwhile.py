#lec 3.3 While Loop to Compute Factorial

print("Enter the number: ")
n=int(input())

i=1
fact=1

while(i<=n):
    fact=fact*i
    i=i+1

print(fact)