#lec 3.11 Nested For loop

s="VIBGYOR"
t="VIBGYOR"
count=0
for i in range(7):
    for j in range(7):
        print(i,j,s[i],t[j])
        count+=1

print("The number of ways in which Sharad and Tarun can wear different color outfits is",count)