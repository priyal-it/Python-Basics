#lec 08: Introduction to if statement

print("Enter your date of birth")
birth_year=int(input())

current_year=2024
age=current_year-birth_year

if(age<13):
    print("You are under age, you cannot watch this movie.")
    print("wait until you are old enough to watch this movie.")
else: 
    print("You are old enough to watch avengers.")
    print("Dont forget to watch the sequels and prequels.")

print("Have a nice time")