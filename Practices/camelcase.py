import re

def camelcase(s):
    return 1 + len(re.findall("[A-Z]", s))
    # retrun a

s = "saveChangesInTheEditor"

print(camelcase(s))
