# Method - 1

a = int(input())
b = int(input())


def lcm(a,b):
    return a*b//gcd(a,b)


def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a%b)

print(lcm(a,b))

