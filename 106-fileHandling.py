#Practical 106: File Handling
def isFound(num):
    f=open('phone_numbers.csv','r')
    s='0'
    found=False
    while(s!=''):
        s=f.readline().strip()
        if(str(num)==s):
            found=True
            break
    return found

def printresult(num):
    if isFound(num):
        print("The number was found.")
    else:
        print("The number was not found.")

printresult("9260104558")
