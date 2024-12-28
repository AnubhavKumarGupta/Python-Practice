#  Python | Multiply all numbers in the list

# Approach 1
l = [1, 2, 3, 4, 5]
mul = 1
for i in l:
    mul *= i
print(mul)


# Approach 2
l = [1, 2, 3, 4, 5]
mul = 1
for i in range(len(l)):
    mul *= l[i]
print(mul)


# Approach 3
l = [1, 2, 3, 4, 5]
mul = 1
i = 0
while i < len(l):
    mul *= l[i]
    i += 1
print(mul)
