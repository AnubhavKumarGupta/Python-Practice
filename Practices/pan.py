import re

def pan(s):
    if s.isupper():
        len(re.findall("[0-9A-Z]", s)) == 10
        return "YES"
    else:
        return "NO"

s = input()
r
print(pan(s))
