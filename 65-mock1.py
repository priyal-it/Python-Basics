'''oppe 1: A data entry operator has a faulty keyboard. The keys 0 and 1 are very unreliable. Sometimes they work, sometimes they don't. While entering phone numbers into a database, the operator uses the letter 'l' as a replacement for 1 and 'o' as a replacement for 0 whenever these binary digits let him down. Both 'l' and 'o' are in lower case. 'l' is the first letter of the word 'land' and not capital 'i'.

Accept a ten-digit number as input. Find the number of places where the numbers 0 and 1 have been replaced by letters. If there are no such replacements, print the string No mistakes. If not, print the number of mistakes (replacements) and in the next line., print the correct phone number.

Test case 1: input=987o35l7o4
output - 3 Mistakes
         9870351704
Test case 2: input=9870351704
output - No Mistakes

'''

n=input("Enter your phone number: ")
count=0
real_num=''
for x in n:
    if x=='l':
        real_num+='1'
        count+=1
    elif x=='o':
        real_num+='0'
        count+=1
    else:
        real_num+=x

if count==0:
    print("No Mistakes")
else:
    print("{0} Mistakes.".format(count))
    print(real_num)