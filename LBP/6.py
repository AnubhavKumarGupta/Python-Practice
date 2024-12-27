def cof(a):
    if a >= 6 and a < 12:
        return a + 1
    elif a >= 12:
        return a + 2
    else:
        return a


n = int(input())

print(cof(n))
