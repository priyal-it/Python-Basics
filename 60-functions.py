#lec 4.8 Intrduction to Functins

#defining a function
def add(a,b):
    ans=a+b
    return ans

print(add(1,8))

def sub(a,b):
    sub=a-b
    print(sub)

print(sub(10,8))
print(sub(8,10))

def discount(cost,d):
    cost1=cost-cost*(d/100)
    return cost1

x=int(input(("Enter the discount percentage: ")))
y=int(input("Enter the cost: "))
print(discount(y,x))