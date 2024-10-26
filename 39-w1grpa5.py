age = int(input()) # int: Read a number as integer from standard input
dob = str(input()) # str: Read a string of format dd/mm/yy from standard input
day, month, year = dob[0:2], dob[3:5], dob[6:8] # int, int, int: Get the correct parts from dob as int

fifth_birthday = str(int(day)) + "/" + str(int(month)) + "/" + str((int(year) + 5) % 100) # Fifth birthday formatted as day/month/year 

last_birthday = str(int(day)) + "/" + str(int(month)) + "/" + str((2024 - age) % 100) # Last birthday formatted as day/month/year

tenth_month_num = (int(month) + 10 - 1) % 12 + 1 # Calculate the month after 10 months
if int(month) + 10 > 12:
    tenth_year = str(int(year) + 1) # Increment the year
else:
    tenth_year = year # Use the same year

tenth_month = str(int(day)) + "/" + str(tenth_month_num) + "/" + str(int(tenth_year) % 100) # str: dob same day after 10 months formatted as day/month/year 

# Print tenth_month, fifth_birthday, and last_birthday in same line separated by comma and a space
print(tenth_month + ", " + fifth_birthday + ", " + last_birthday)

weight = float(input()) # float: Read a number as float from stdin(Standard input)

kg = int(weight)
grams = int((weight - kg) * 1000)
weight_readable = str(kg) + " kg " + str(grams) + " grams" # str: reformat weight of format 55 kg 250 grams

# Print weight_readable 
print(weight_readable)
