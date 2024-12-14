#lec 5.9 Generator

def square(limit):
    x=0
    while(x<limit):
        yield x*x
        yield x*x*x
        x+=1

limit=int(input("Enter the limit: "))

a=square(limit)

print(next(a),next(a))
print(next(a),next(a))
print(next(a),next(a))
print(next(a),next(a))
print(next(a),next(a))
print(next(a),next(a))
