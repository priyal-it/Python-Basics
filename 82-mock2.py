#function to check whether a number is prime or not

def isPrime(n):
    for i in range(2,n//2+1):
        if(n%i==0):
            return False
            break
    return True

def list_prime(L):
    primeL=[]
    for i in range(2,len(L)+1):
        if isPrime(i):
            primeL.append(i)
    return primeL

def prime_galore(L):
    a=0
    for i in list_prime(L):
        if isPrime(L[i]):
            a+=1
    return a

L=[1, 3, 11, 18, 17, 5, 6, 8, 10]
print(prime_galore(L)) #answer = 2
M=[1, 2, 3, 4, 5, 6, 7, 8, 9]
print(prime_galore(M)) #answer = 1