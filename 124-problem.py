#Practical 124: Finding total marks of the topper from scores.csv
# Problem statement: What are the total marks of the topper from this scores dataset? (Without Using Pandas)

f=open('Python-Basics/FileHandling/scores.csv','r')
scores=f.readlines()[1:]
max=0
for record in scores:
    fields=record.split(',')
    if int(fields[8])>max:
        max=int(fields[8])
print(max)
    