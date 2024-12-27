import re


def fun(s):
    return len(re.findall("[aeiou]", s))


s = input("Enter any string: ")
print(s)
print(fun(s))
