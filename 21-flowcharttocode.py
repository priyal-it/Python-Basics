#lec 09: problem 4- Converting a flowchart into python code

#start
print("Enter the time of travelling in minutes: ")
time=int(input())
longer=30
shorter=longer
print("Enter the cost of travelling: ")
higher=50
lower=higher
price=int(input())
if(time>=longer):
    if(price<lower):
        print("Coach")
    elif(price>=higher):
        print("train")
    
elif(time<=shorter):
    if(price<lower):
        print("Red Eye Flight")
    elif(price>=higher):
        print("Daytime flight")