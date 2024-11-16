'''A square matrix M is said to be:
diagonal: if the entries outside the main-diagonal elements are equal
scalar: if it is a diagonal matrix, all of whose diagonal elements are equal
identity: if it is a scalar matrix, all of whose diagonal elements are equal to 1

Write a function named matrix_type that accepts a matrix M as argument and returns the type of matrix. It should be one of these strings: diagonal, scalar, identity, non-diagonal. The type you ouput should be the most appropriate one for the given matrix. 

You do not have to accept input from the user or print output to the console. You just have to wite the function definition.

'''
def matrix_type(M):
    B=M[0][0]
    Identity=0
    scalar=0

    for i in range(len(M)): #0,1,2
        for j in range(len(M)): #0,1,2
            if(i != j):
                if M[i][j]!=0:
                    return("Non-diagonal")
                elif(M[i][j]==1):
                    Identity+=1
                elif M[i][j]==0:
                    scalar+=1
    if Identity==len(M):
        return("Identity")
    else:
        if scalar==len(M):
            return ("Scalar")
        else:
            return ("Diagonal")