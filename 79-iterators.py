#lec 5.9: Iterators

fruits=['mango','apple','banana','orange','pineapple','watermelon','guava','kiwi']

for fruit in fruits:
    print(fruit)

basket=iter(fruits)

print(next(basket))
print(next(basket))