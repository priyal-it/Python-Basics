#Problem 1: Write a python program using function which calculates the number of uppercase letters, lowercase  letters, total number of characters and number of words.

def noOfUpper(text):
    result=0
    if text:
        for t in text:
            if str.isalpha(t) and t.upper()==t:
                result+=1
    return result

def noOfLower(text):
    result=0
    if text:
        for t in text:
            if str.isalpha(t) and t.lower()==t:
                result+=1
    return result
    
def totalNo(text):
    result=0
    if text:
        for t in text:
            if t!=" ":
                result+=1
    return result
    
def noOfWords(text):
    text=text.split(" ")
    return len(text)

text=input("Enter a piece of string: ")

print(f"Number of Uppercase Letters: {noOfUpper(text)}")
print(f"Number of Lowercase Letters: {noOfLower(text)}")
print(f"Number of Characters: {totalNo(text)}")
print(f"Number of Words: {noOfWords(text)}")
