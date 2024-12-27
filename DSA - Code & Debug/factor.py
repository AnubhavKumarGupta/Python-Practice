n = int(input())


# l = []
# for i in range(1, n + 1):
#     if n % i == 0:
#         l.append(i)
# print(l)


# l = []
# for i in range(1, n // 2 + 1):
#     if n % i == 0:
#         l.append(i)
# l.append(n)
# print(l)


import math as m

l = []
for i in range(1, int(m.sqrt(n)) + 1):
    if n % i == 0:
        l.append(i)
        if n // i != i:  
            l.append(n // i)
print(sorted(l))
