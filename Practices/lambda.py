s = lambda a, b: a if a > b else b
print(s(-1, -2))

s = lambda a, b, c: a if a > b and a > c else b if b > c and b > a else c
print(s(-1, -2, -3))
