#Practical 110: Using Recursion to find the Sum of First n Numbers
def sum(n):
    if n==1:
        return 1
    for i in range(n):
        return n+sum(n-1)
n=int(input("Enter a number: "))
print(f"The sum of first{n} numbers is {sum(n)}")