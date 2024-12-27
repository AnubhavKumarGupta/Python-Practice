import re


def rege(a):
    return len(re.findall("[a-zA-Z0-9]", a))


a = "Anubhav Kumar @ 3 4 5 6 % ^ & * ( ) _ + > < ? | ! ~ ~ ~ ` @ # # # # Gupta"

print(rege(a))
