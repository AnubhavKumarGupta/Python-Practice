n = int(input())


def fac(a):
    if a in [0, 1]:
        return 1
    return a * fac(a - 1)


print(fac(n))
