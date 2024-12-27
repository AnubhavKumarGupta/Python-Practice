import re


def rege(a):
    return len(re.findall("\s", a))


a = "Anubhav Kumar Gupta"

print(rege(a))
