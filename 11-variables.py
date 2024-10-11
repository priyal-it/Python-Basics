#lec 02: variables-a programmers perspective (defining variables and adding comments)
ram_bank_balance=100000
#ram's bank balance, note that this is positive
ram_loan=500000
#ram's loan, this is to be returned by him and hence will count as negative

lakshman_bank_balance=2000000
lakshman_loan=1000000

net_income=ram_bank_balance+lakshman_bank_balance
#net income is the total bank balance of the two brothers
net_liability=ram_loan+lakshman_loan
#net liability is the total loan of the brothers

final_value=net_income-net_liability
#final valueu is the family's final money (could be +ve or -ve)
print("So, the family has",final_value)

#lec 03: variables revisited (dynamic typing)
n=11
print(type(n))

n=n/2
print(int(n))
print(type(n))