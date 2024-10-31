#lec 3.9: Formatted Printing

#print statement inside loop
#printing 1-10 with proper format
for x in range(10):
    if(x<9):
        print(x+1,end=', ')
    elif(x==9):
        print(x+1, end='.')

#separator in print statement
d=31
m=10
y=2024

print("Today's date is: ",end='')
print(d,m,y,sep='-')

#formatted printing in print statement
num=int(input("Enter a number: "))
for i in range(1,11):
    #print(num,'x',i,'=',num*i)
    #print(f'{num} x {i} = {num*i}')
    #print("{0} x {1} = {2}".format(num,i,num*i))
    print("%d x %d = %d" %(num,i,num*i))

#printing numbers
pi=22/7
print(f"Value of Pi = {pi:.4f}")
print("Value of Pi = {0}".format(pi))
print("Value of pi = %f" %(pi))

#printing a pattern of numbers
print("{0:5d}".format(1))
print("{0:6d}".format(11))
print("{0:7d}".format(111))
print("{0:8d}".format(1111))
print("{0:9d}".format(11111))