#  Python program to find second largest number in a list


# Approach 1
l = [1, 2, 9, 3, 4, 56, 8, -1]
l.sort()
print(l[-2])


# Approach 2
l = [1, 2, 19, 3, 4, 56, 8, -1]
first = second = float("-inf")
for i in l:
    if i > first:
        second = first
        first = i
    elif i > second and i != first:
        second = i
print(second)
