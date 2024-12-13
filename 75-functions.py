#lec 5.8: Write a Python code using functions which calculates the number of upper case letters, lower case letters, total number of characters and number of words
def no_upper(s):
    i=0
    for x in s:
        if x.isupper():
            i+=1
    return i

def no_lower(s):
    i=0
    for x in s:
        if x.islower():
            i+=1
    return i

def no_char(s):
    i=0
    for x in s:
        i+=1
    return i

def no_words(s):
    i=1
    for x in s:
        if x == ' ':
            i+=1
    return i
s=input("Enter a string: ")
print('The number of uppercase letters in the string is {0}'.format(no_upper(s)))
print('The number of lowercase letters in the string is {0}'.format(no_lower(s)))
print('The number of characters in the string is {0}'.format(no_char(s)))
print('The total number of words in the string is {0}'.format(no_words(s)))