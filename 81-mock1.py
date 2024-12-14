'''Papers is a list of tuples that contains information about the number of papers published by a researcher during his career. Each element is of the form (year,num): the researcher has published (num) papers in the (year) year.

Write a function named good_years hat accepts (papers) as argument and returns the list of years in which the researcher has published the maximum number of papers. 
'''

def good_years(papers):
    max_val=0
    for x in papers:
        if x[1]>max_val:
            max_val=x[1]
    years=[]
    for x in papers:
        if x[1]==max_val:
            years.append(x[0])
    return years

papers=[(2024,15),(2023,25),(2022,20),(2021,25),(2020,15)]

print(good_years(papers))