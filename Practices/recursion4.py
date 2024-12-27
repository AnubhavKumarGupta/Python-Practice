def fac(n):
    if n in [0, 1]:
        return n
    else:
        return n * fac(n - 1)


print(fac(25))
