"""
OTP generator: Generate an OTP given its length.
"""

import random
def otpG(n):
    otp=""
    for i in range (n):
        otp+=str(random.randint(0,9))
    return otp
n=int(input("Enter the length: "))

print(otpG(n))