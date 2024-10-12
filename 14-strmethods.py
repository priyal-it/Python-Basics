#lec 06: String Methods

#1. lower()
x="hELLO wORLD!"
print(x.lower())

#2. upper()
x="hELLO wOrld!"
print(x.upper())

#3. capitalize()
x="heLLO woRlD!"
print(x.capitalize())

#4. title()
x="heLLO woRlD!"
print(x.title())

#5.w swapcase
x="heLLO woRlD!"
print(x.swapcase())

#6. islower()
x="heLLO woRlD!"
y="hello world!"
print(x.islower())
print(y.islower())

#7. isupper()
x="heLLO woRlD!"
y="HELLO WORLD!"
print(x.isupper())
print(y.isupper())

#8. istitle()
x="Hello world!"
y="Hello WorlD!"
z="Hello World!"
print(x.istitle())
print(y.istitle())
print(z.istitle())

#9. isdigit()
x="123o"
y='123'
z='abc'
print("isdigit()")
print(x.isdigit())
print(y.isdigit())
print(z.isdigit())

#10. isalpha()
x="123o"
y='123'
z='abc'
print("isalpha")
print(x.isalpha())
print(y.isalpha())
print(z.isalpha())

#11. isalnum()
x="123!o"
y='123'
z='abc'
print('isalnum')
print(x.isalnum())
print(y.isalnum())
print(z.isalnum())

#12. strip()
x="...python___"
y="___python___"
print(x.strip('.'))
print(x.strip('_'))
print(y.strip("_"))

#13. lstrip()
x="...python..."
print(x.lstrip('.'))

#14. rstrip()
print(x.rstrip('.'))

#15. startswith()
x="python"
print(x.startswith("p"))
print(x.startswith('P'))
print(x.startswith('2'))

#16. endswith()
x="PythoN"
print(x.endswith("n"))
print(x.endswith("N"))
print(x.endswith("!"))

#17 count()
x="Sheep"
y="sheEp"
print(x.count('e'))
print(x.count("E"))
print(y.count("E"))
print(y.count("e"))

#18. index()
x="Sheep"
y="ShEep"
print(x.index("e"))
print(y.index('E'))
print(y.index('e')+1)

#19. replace()
x="Sheep"
y="ShEep"
print(x.replace('S',"s"))
print(y.replace('E','e'))
y=y.replace('S','s')
y=y.replace('E',"e")
print(y)