import re

s = input()
a = re.fullmatch("[a-zA-Z0-9_.]*@gmail.com", s)

if a != None:
    print("Valid")
else:
    print("Invalid")
