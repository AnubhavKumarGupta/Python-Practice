n = int(input())


def po(n, m):
    if m == 1:
        return n
    else:
        return n * po(n, m - 1)


print(po(2, n))
