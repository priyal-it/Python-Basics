#week3 GrPA 2: For loop
# Note this prefix code is to verify that you are not using any for loops in this exercise. This won't affect any other functionality of the program.
with open(__file__) as f:
    content = f.read().split("# <eoi>")[2]
if "while " in content:
    print("You should not use while loop or the word while anywhere in this exercise")

# your code should not use more than 7 for loops 
# assuming one for loop per problem
if content.count("for ")>7:
    print("You should not use more than 7 for loops")

# This is the first line of the exercise
task = input()
# <eoi>

if task == 'factorial':
    n = int(input())
    result = 1

    for i in range(1,n+1):
        result*=i
    print(result)
elif task == 'even_numbers':
    n = int(input())

    for i in range(0, n+1,2):
        print(i)

elif task == 'power_sequence':
    n = int(input())
    result = 1

    for i in range(n):
        print(result)
        result *= 2

elif task == 'sum_not_divisible':

    n = int(input())
    total = 0
    for i in range(1, n):
        if i % 4 != 0 and i % 5 != 0:
            total += i
    print(total)

elif task == 'from_k':

    n = int(input())
    k = int(input())
    count = 0
    for i in range(k, 0, -1):
        i_str = str(i)
        if '5' not in i_str and '9' not in i_str and i % 2 != 0:
            print(i_str[::-1])
            count += 1
            if count == n:
                break

elif task == 'string_iter':

    s = input()
    prev = 1
    for char in s:
        num = int(char)
        print(num * prev)
        prev = num

elif task == 'list_iter':
    lst = eval(input()) # this will load the list from input
    for element in lst:
        print(f'{element} - type: {type(element)}')

else:
    print("Invalid")
