#expression x^2+x+41 is divisible by 41.
x=1
while ((x**2)+x+41)%41!=0:
    x+=1

print("The smallest value of x for which the expression x^2+x+41 is divisible by 41 is {0}".format(x))