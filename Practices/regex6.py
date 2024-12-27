import re

s = input()
m = re.findall("[^aeiou]", s)

print(m)
