#lec 3.7 for loop for multiplication tables

n=int(input("Enter a number: "))

for i in range(10):
    print(n,"x",i+1,"=",n*(i+1))