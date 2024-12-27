a, b = map(int, input().split())

l = []

for i in range(a, b + 1):
    l.append(i * i * i)

print(sum(l))
