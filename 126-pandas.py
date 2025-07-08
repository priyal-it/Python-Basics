#Practical 124: Finding total marks of the topper from scores.csv using Pandas
# Problem statement: What are the total marks of the topper from this scores dataset? (Using Pandas)

import pandas as pd
scores=pd.read_csv('Python-Basics/FileHandling/scores.csv')
print(scores['Total'].max())