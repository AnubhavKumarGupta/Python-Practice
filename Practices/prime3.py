a = int(input())


def prime(a):
    # if a <= 1:
    #     return False
    for i in range(1, int(a / 2) + 1):
        if a % i == 0:
            return False
    return True


print(prime(a))
