#Practical 109: Sum of First n Numbers
def sum(n):
    result=0
    for i in range(n):
        result+=i+1
    return result
n=int(input("Enter a number: "))
print(f"Sum of First {n} numbers is {sum(n)}")