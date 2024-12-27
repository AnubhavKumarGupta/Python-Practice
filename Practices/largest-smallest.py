a = int(input("start: "))
b = int(input("end: "))

l = []
for i in range(a, b + 1):
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            break
    else:
        l.append(i)

m = max(l)
s = min(l)
print(m - s)





