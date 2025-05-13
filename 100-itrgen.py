#Iterators and Generators
#iterators

lst=["apple", "mango", "cherry"]
basket=iter(lst)
print(next(basket))
print(next(basket))

#generator

def gen_itr(n):
    x=0
    while x<n:
        yield x
        yield x*x
        yield x*x*x
        x+=1

a=gen_itr(10)

print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))