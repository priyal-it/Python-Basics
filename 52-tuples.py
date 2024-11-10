#lec 4.3 tuples

import string
l=list(range(10))

t=tuple(range(10))

print(l)
print(t)

l.remove(0) #not possible with tuple
print(l)

print(string.ascii_letters)
s=string.ascii_letters
print(list(s))