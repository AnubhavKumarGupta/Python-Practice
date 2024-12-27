n = [1, 2, 90, 10, 110]

l = []

for i in range(len(n) - 1):
    for j in range(i + 1, len(n) - 1):
        l.append(j - i)

print(l)
