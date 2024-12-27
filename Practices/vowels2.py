import re


def fun(s):
    count = 0
    for i in s:
        if i in "(a,e,i,o,u)":
            count = count + 1
    return count


s = input("Enter any string: ")
print(s)
print(fun(s))
