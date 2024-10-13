print("Enter your marks:")
a=int(input())
if(a>=0 and a<=100):
# >=90 - A
    if(a>=90):
        print("Grade: A")
    if(a<90 and a>=80):
        print("Grade: B")
    if(a<80 and a>=70):
        print("Grade: C")
    if(a<70 and a>=60):
        print("Grade: D")
    if(a<60 and a>=0):
        print("Grade: E")

else:
    print("Enter valid marks.")