import re

n = input()
n.lower()

s = re.sub("[aeiou]", ".", n)
print(s)
