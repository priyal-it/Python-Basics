#w2grpa4
#operation = input()

if operation == "odd_num_check":
    num = int(input())
    result = "yes" if num % 2 != 0 else "no"
    print(result)

elif operation == "perfect_square_check":
    num = int(input())
    sq_num = int(num**0.5)
    result = "yes" if sq_num**2 == num else "no"
    print(result)

elif operation == "vowel_check":
    text = input()
    result = "no"
    for ch in text.lower():
        if ch in ['a','e','i','o','u']: 
            result = "yes"
    print(result)

elif operation == "divisibility_check":
    num = int(input())
    if num % 2 == 0 and num % 3 == 0:
        print("divisible by 2 and 3")
    elif num % 2 == 0:
        print("divisible by 2")
    elif num % 3 == 0:
        print("divisible by 3")
    else:
        print("not divisible by 2 and 3")

elif operation == "palindrominator":
    text = input()
    text += text[-2::-1]
    print(text)

elif operation == "simple_interest":
    principal_amount = int(input())
    n_years = int(input())
    if n_years < 10:
        result = round(n_years * principal_amount * 0.05)
    else:
        result = round(n_years * principal_amount * 0.08)
    print(result)
    
else:
    print("Invalid Operation")