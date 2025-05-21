#Practical 108: Caesar Cipher Decoder
import string
def create_decoder_dict():
    l=string.ascii_lowercase
    l=list(l)
    d={}
    for i in range(len(l)):
        d[l[i]]=l[(i-3)%26]
    return d

f=open('encrypted.txt','r')
g=open('decoded.txt','w')
d=create_decoder_dict()

c=f.read(1)
while (c!=''):
    g.write(d[c])
    c=f.read(1)

f.close()
g.close()