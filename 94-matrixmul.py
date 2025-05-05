def matrixmul(A,B):
    X=[[0,0,0],[0,0,0],[0,0,0]]
    for i in range(3):
        for j in range(3):
            X[i][j]=0
            for k in range(3):
                X[i][j]+=A[i][k]*B[k][j]
    return X

A=[[0,0,0],[0,0,0],[0,0,0]]
B=[[0,0,0],[0,0,0],[0,0,0]]
print("Enter matrix A: ")
for i in range(3):
    for j in range(3):
        A[i][j]=int(input("Enter element A[%d][%d]: "%(i,j)))
print("Enter matrix B: ")
for i in range(3):
    for j in range(3):
        B[i][j]=int(input("Enter element B[%d][%d]: "%(i,j)))

print("Matrix A: ")
for i in range(3):
    for j in range(3):
        print(A[i][j],end=" ")
    print()
print("Matrix B: ")
for i in range(3):
    for j in range(3):
        print(B[i][j],end=" ")
    print()
print("Matrix A*B: ", matrixmul(A,B))