''' A sequence of integers of even length is said to be left-heavy if the sum of the terms in the left-half of the sequence is greater than the sum of the terms in the right half. It is termed right-heavy if the sum of the second half is greater than the first half. It is said to be balanced if both the sums are equal.

Accept a sequence of comma-separated integers as input. Determine if the sequence is left-heavy, right-heavy or balanced and print this as the output.

Test case 1: 
input: 1,2,3,4,5,6
output: right-heavy

input: 1,1,1,1
output: balanced
'''

l=[]
l=input().split(',')
n=len(l)
right_sum=0
left_sum=0
for i in range(0,n):
    if i<n/2:
        left_sum+=int(l[i])
    elif i>=n/2:
        right_sum+=int(l[i])
    
if(right_sum>left_sum):
    print("right-heavy")
elif(right_sum<left_sum):
    print("left-heavy")
elif(right_sum==left_sum):
    print("balanced")