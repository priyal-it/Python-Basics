#lec 3.4 Introduction to for loop

n=int(input("Enter a number: "))

for i in range(n):
    if(i%2==0):
        print(i+1,"Hello World!")
    else:
        print(i+1,"Hi World!")