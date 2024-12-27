# Program to interchange first and last elements in a list

# 1st way

# n = eval(input())
# a = []
# f = n[0]
# l = n[-1]

# a.append(f)
# a.append(n[1 : len(n) - 1])
# a.append(l)

# print(a)

# 2nd way

n = eval(input())
n[0], n[-1] = n[-1], n[0]
print(n)

