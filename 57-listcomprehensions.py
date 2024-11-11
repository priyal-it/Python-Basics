#lec 4.7 List Comprehensions

a=10
b=20
if a < b:
    small=a
else:
    small=b

print(small)

#replacement of above multi-line code to a single line
small =a if a<b else b
print(small)

a=5
while a>0:
    print(a)
    a-=1

#replacement of above multi-line code to a single line
b=5
while b>0: print(b); b-=1

fruits = ['mango','apple','banana','orange','pineapple','watermelon','guava','kiwi']

newList=[]
for fruit in fruits:
    if 'n' in fruit:
        newList.append(fruit.capitalize())
print(newList)

#replacement of above multi-line code to a single line
newList=[fruit.capitalize() for fruit in fruits if 'n' in fruit]
print(newList)