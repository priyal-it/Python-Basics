#importing libraries

import math
import random

print(math.log(10))
print(math.sin(45))
print(math.sqrt(16))
print(math.sqrt(65))
print(math.factorial(4))
print()
print(random.random())

#tossing a coin simulator
a=random.random()
if(a>0.5):
    print("Head")
else:
    print("Tail")