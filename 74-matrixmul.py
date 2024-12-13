#lec 5.4 Matrix multiplication

#3x3 matrix multiplication

'''
a= a00 a01 a02
   a10 a11 a12
   a20 a21 a22

b= b00 b01 b02
   b10 b11 b12
   b20 b21 b22

multiplication of a and b
mul[i][j]
mul[0][0] = a00*b00 + a01*b10 + a02*b20
mul[0][1] = a00*b01 + a01*b11 + a02*b21
mul[0][2] = a00*b02 + a01*b12 + a02*b22
mul[1][0] = a10*b00 + a11*b10 + a12*b20
mul[1][1] = a10*b01 + a11*b11 + a12*b21
mul[1][2] = a10*b02 + a11*b12 + a12*b22
mul[2][0] = a20*b00 + a21*b10 + a22*b20
mul[2][1] = a20*b01 + a21*b11 + a22*b21
mul[2][2] = a20*b02 + a21*b12 + a22*b22
'''
a = [[1,2,3],[4,5,6],[7,8,9]]
b = [[9,8,7],[6,5,4],[3,2,1]]
mul=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(3):
    for j in range(3):
        mul[i][j]=a[i][0]*b[0][j] + a[i][1]*b[1][j] + a[i][2]*b[2][j]

print(mul)