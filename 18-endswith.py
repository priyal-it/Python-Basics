#find whether the given number ends with 0 or 5 or any other number.

print("Enter a number:")
x=int(input())

if(x%5==0):
    if(x%10==0):
        print("The number ends with 0.")
    else:
        print("The number ends with 5.")
else:
    print("Other.")