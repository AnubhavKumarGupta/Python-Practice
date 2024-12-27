t, b = map(int, input().split())
for _ in range(t):
    a = [int(x) for x in input().split()]  # important line
    l = []
    for i in a:
        if i > b:
            l.append(i)

print(len(l))
