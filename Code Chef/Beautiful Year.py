# n = int(input())

# if n < 2013:
#     print(2013)

# else:
#     print(n + 1)


s = int(input()) + 1
while len(set(str(s))) < 4:
    s += 1
print(s)
