n = int(input())


def rec(n):
    if n < 10:
        return n
    return n % 10 + rec(n // 10)

print(rec(n))