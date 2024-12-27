import re

s = input()
t = input()
m = re.match(t, s)
if m != None:
    print("Available")
else:
    print("Not Available")
