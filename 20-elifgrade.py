print("Enter your marks:")
a=int(input())
if(a>=0 and a<=100):
# >=90 - A
    if(a>=90):
        print("Grade: A")
    elif(a<90 and a>=80):
        print("Grade: B")
    elif(a<80 and a>=70):
        print("Grade: C")
    elif(a<70 and a>=60):
        print("Grade: D")
    elif(a<60 and a>=0):
        print("Grade: E")

else:
    print("Enter valid marks.")