l = [5, 6, 7, 7, 1, 9, 111, 1, 1, 5, 1, 1]

d = {}

for i in range(0, len(l)):
    if l[i] in d:
        d[l[i]] += 1
    else:
        d[l[i]] = 1

print(d)

# print(d[1])
