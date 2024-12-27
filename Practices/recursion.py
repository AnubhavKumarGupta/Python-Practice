def fac(a):
    if a == 1 or a == 0:
        return 1
    else:
        return a * fac(a - 1)


a = int(input())

print(f"The Factorial of the given number is {a}= ", fac(a))
