#Practical 107: Caesar Cipher
import string

def create_cipher_dict():
    l=string.ascii_lowercase
    l=list(l)
    d={}
    for i in range(len(l)):
        d[l[i]]=l[(i+3)%26]
    return d

f=open('file.txt','r')
g=open('output.txt','w')
d=create_cipher_dict()

c=f.read(1)

while(c!=''):
    g.write(d[c])
    c=f.read(1)

f.close()
g.close()