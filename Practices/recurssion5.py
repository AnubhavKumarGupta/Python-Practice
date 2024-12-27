def power(b, p):
    if p == 0:
        return 1
    return b * power(b,p - 1)


b = int(input())
p = int(input())

print(power(b, p))
