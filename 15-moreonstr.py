#lec 07: an interesting cipher- more on strings
alpha="abcdefghijklmnopqrstuvwxyz"
i=20
print(alpha[i])
print(alpha[i+1])
print(alpha[i+2])
print(alpha[i+3])

i=25
print(alpha[i%26])
print(alpha[(i+1)%26])
print(alpha[(i+2)%26])
print(alpha[(i+3)%26])