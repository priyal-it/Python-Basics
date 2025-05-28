#Practical 113: Obvious Search Method
def obvious_search(l,a):
    for x in l:
        if x==a:
            print("The element was found.")
            Found=True
            break
        else:
            Found=False
    return Found

l=[123,34,5,23,4234,5234,23]
print(obvious_search(l,123))