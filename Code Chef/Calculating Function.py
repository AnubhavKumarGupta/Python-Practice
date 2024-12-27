a = int(input())
p = []
n = []
for i in range(1, a + 1):
    if i % 2 != 0:
        p.append(i)
    else:
        n.append(i)


N = sum(p)
P = sum(n)

print(P - N)
