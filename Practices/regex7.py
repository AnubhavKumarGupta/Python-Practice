import re

s = input()
m = re.finditer("[a-z]", s)

print(m)
