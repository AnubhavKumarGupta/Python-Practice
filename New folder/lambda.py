A= lambda a, b, c:  a if (a > b and a > c) else b if (b > c and b > a) else c

print(A(10,11,19))
