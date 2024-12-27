import re

n = input("Enter the String ")

n1 = n.lower()
a = len(re.findall("[aeiou]", n1))

print(a)
