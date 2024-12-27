a = input()
b = []
c = ""
d = 0

for i in a:
    if i not in b:
        b.append(i)

for ele in b:
    count = 0
    for l in range(len(a)):
        if ele == a[l]:
            count += 1
        if count > d:
            d = count
            c = ele
print(c)
