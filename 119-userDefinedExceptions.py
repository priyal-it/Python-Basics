#Practical 119: User-defined Exceptions
a=int(input("Enter your age: "))
if a>18:
    print("You are eligible for voting.")
else:
    raise Exception("You are underage and ineligible for voting.")