#Problem 4: Check whether the entered number is a Palindrome or not

n1=int(input("Enter the number to check: "))

n=str(n1)
digits=len(n)

i=0

isPalindrome=1
while(i<digits/2):
    if(n[i]!=n[digits-i-1]):
        isPalindrome=0
        break
        
    i=i+1

if(isPalindrome==0):
    print("The entered number is not a Palindrome.")
elif(isPalindrome==1):
    print("The entered number is a Palindrome.")