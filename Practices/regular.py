import re

count = 0
ma = re.finditer("ab", "aababbrhbb")
for m in ma:
    print(m.group())
    count += 1 + 2
print(count)
