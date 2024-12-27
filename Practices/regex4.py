import re

s = input()
t = input()
m = re.fullmatch(t, s)
if m != None:
    print("Full Match")
else:
    print("Match")
