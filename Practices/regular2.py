import re

def mes(s):
    return len(re.findall("[a-zA-z0-9]", s))


# s = "Abfd@3#c"

s = "ABFD@3#c"

print(mes(s))
