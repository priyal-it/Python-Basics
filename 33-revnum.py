#Problem 3: Reverse the digits in the given number

n1=int(input('Enter a number: '))

n=abs(n1)
rev=n%10
n=n//10
while(n>0):
    r=n%10
    n=n//10
    rev=rev*10+r

if(n1>=0):
    print(rev)
if(n1<0):
    print('-',rev)

