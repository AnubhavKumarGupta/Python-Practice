n = int(input())


def rec(n):
    if n <= 1:
        return n
    return rec(n - 1) + n


print(rec(n))
