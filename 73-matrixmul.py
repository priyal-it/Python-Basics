#lec 5.4 Matrix multiplication

#2 by 2 multiplication

#let a and b be two different matrices

'''
a= a00 a01  b= b00 b01
   a10 a11     b10 b11

mul= a00*b00 + a01*b10  a00*b01 + a01*b11
     a10*b00 + a11+b10  a10*b01 + a11*b11

'''

#declare two matrices
a=[[1,2],[3,4]]
b=[[5,6],[7,8]]

#multiplication

'''
mul[i][j]        
mul[0][0]=a00*b00 + a01*b10
mul[0][1]=a00*b01 + a01*b11
mul[1][0]=a10*b00 + a11+b10
mul[1][1]=a10*b01 + a11*b11
'''
i=0
j=0
mul=[[0,0],[0,0]]
for i in range(2):
    for j in range(2):
        mul[i][j]=a[i][0]*b[0][j] + a[i][1]*b[1][j]
print(mul)

#multiplication but, using a function for it

def matrix_mul(a,b):
    i=0
    j=0
    mul=[[0,0],[0,0]]
    for i in range(2):
        for j in range(2):
            mul[i][j]=a[i][0]*b[0][j] + a[i][1]*b[1][j]
    return mul

print(matrix_mul(a,b))