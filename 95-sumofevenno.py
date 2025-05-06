#Practical 95: Write a Python program to find the sum of all even numbers from 1 to 100.
def sum_of_even_numbers(n):
    sum=0
    for i in range(n+1):
        if i%2==0:
            sum+=i
    return sum
print(sum_of_even_numbers(100))