import random

#generating a random two digit number
a=100*random.random()
a=int(a)

while True:
    print("Enter a guess: ")
    b=int(input())
    if(b==a):
        print("Your guess is correct.")
        break
    elif(b<a):
        print("Guess a little higher.")
    elif(b>a):
        print("Guess a little lower.")
