#lec 3.13 break, continue and pass

#break
#Program that returns the username part from an email address entered by the user
email=input("Enter your email address: ")

for c in email:
    if(c=='@'):
        break
    print(c,end="")

#continue
#Program that returns the username and domain name from an email address entered by the user
email2=input("Enter your email address: ")

for c in email2:
    if(c=='@'):
        print('')
        continue
    print(c,end="")

#pass
for i in range(11):
    if(i%3==0):
        print(i,end=', ')
    else:
        pass