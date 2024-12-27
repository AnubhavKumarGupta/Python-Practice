import re


def fun(s):
    # return len(re.findall("[ ]", s))
    return s.count(" ")


s = input("Enter any string: ")
print(s)
print(fun(s))
