n = int(input())


def Anubhav(a):
    if a in [0, 1]:
        return a
    else:
        return Anubhav(a - 1) + Anubhav(a - 2)


print(Anubhav(n))
