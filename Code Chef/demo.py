n = int(input("Input the Number that you want to check "))


def prime(a):
    if n <= 1:
        return False
    for i in range(2, n):
        if a % i == 0:
            return False
    return True

print(prime(n))
