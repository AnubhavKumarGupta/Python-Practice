import re

s = input()
a = len(re.findall("[A-Z]", s))
print(f"the number of upper case letter in {s} is {a}")
