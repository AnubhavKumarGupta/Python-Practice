n = int(input())



def fib(a):
    if a in [0, 1]:
        return a
    else:
        return fib(a - 1) +  fib(a - 2)


print(fib(n))
