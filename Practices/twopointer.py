n = [1, 0, 1, 0, 0, 1, 0]

s = 0
e = len(n) - 1

while (s < e):
    if n[s] == 0:
        s += 1
    else:
        if n[e] == 0:
            # Swap n[s] and n[e]
            n[s], n[e] = n[e], n[s]
            s += 1
            e -= 1
        else:
            e -= 1

print(n)
