l = 1
h = 10

li = []

for i in range(l, h + 1):
    if i == 0 or i == 1:
        continue
    else:
        for j in range(2, i):
            if i % j == 0:
                break
            else:
                li.append(i)
print(li)
