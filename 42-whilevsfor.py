#Lec 3.10: for loop and while loop comparison

#Problem 1: finding factorial
#factorial using while loop
num = int(input("Enter a number: "))
fact=1
if(num<0):
    print("Not defined")
else:
    while(num>0):
        fact=fact*num
        num-=1
    print(fact)

#factorial using for loop
num = int(input("Enter a number: "))
fact=1
if(num<0):
    print("Not defined")
else:
    for i in range(1,num+1):
        fact=fact*i
        i+=1
    print(fact)

#Problem 2: Find the number of digits in a given number
#While loop

n=int(input("Enter a number: "))
i=0
while(n%10!=0):
    n=n//10
    i=i+1
print(i)

#For loop

n=abs(int(input("Enter a number: ")))
strN=str(n)
i=0
for c in strN:
    i+=1
print(i)

#Problem 3: Reversing the digits of a number

#while loop
num=int(input("Enter a number: "))
absNum=abs(num)
rev=absNum%10
absNum=absNum//10

while(absNum>0):
    r=absNum%10
    absNum=absNum//10
    rev=rev*10 + r

if(num>0):
    print(rev)
else:
    print(rev-2 * rev)

#for loop
num=int(input("Enter a number: "))
absStrNum=str(abs(num))
rev=''
for c in absStrNum:
    rev=c+rev

if(num>=0):
    print(rev)
else:
    print('-'+rev)

#Problem 4: Palindrome checker

#while loop
num=int(input("Enter a number: "))
absNum=abs(num)
rev=absNum%10
absNum=absNum//10
while(absNum>0):
    r=absNum%10
    absNum=absNum//10
    rev=rev*10 + r

if(num<0):
    rev=rev-2*rev
if(rev==num):
    print("Palindrome.")
else:
    print("Not Palindrome.")

#for loop
num=int(input("Enter a number: "))
absStrNum=str(abs(num))
rev=''
for c in absStrNum:
    rev=c+rev
if(num<0):
    rev='-'+rev
if(num==int(rev)):
    print("Palindrome.")
else:
    print("Not Palindrome.")
