#lec 3.12: Tutorial on nested loops

#Problem 1: Find all prime numbers less than the entered number

n=int(input("Enter a number: "))
if(n>2):
    print(2,end=" ")
for i in range(3,n):
    flag=False
    for j in range(2,i):
        if(i%j==0):
            flag=False
            break
        else:
            flag=True
    if(flag):
        print(i,end=" ")

#Problem 2: Find the day wise total rainfall for the entered duration of time e.g. week, month, etc.

days = int(input("Enter the number of days: "))

for i in range(1, days + 1):
    total = 0
    print(f"Day {i}")
    
    while True:
        r = int(input("Enter the rainfall (enter -1 to end the day): "))
        if r == -1:
            break
        total += r
    
    print("The total rainfall for day {0} is {1}".format(i, total))

# Problem 3: Find the length of longest word from the set of words entered by user.

word=input("Enter a word: ")
set=[]
maxLen=0
while(word!='-1'):
    count=0
    for letter in word:
        count=count+1
    if(count>maxLen):
        maxLen=count
    word=input("Enter a word: ")
print("The length of longest word is %s",maxLen)