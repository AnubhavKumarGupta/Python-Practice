n = [5, 10, 3, 2, 50, 80]

t = 40

s = 0
e = len(n) - 1

while s < e:
    if abs(n[s] - n[e]) == t:
        print(n[s], n[e])

    elif abs(n[s] - n[e]) < t:
        s = s + 1

    else:
        e = e - 1
