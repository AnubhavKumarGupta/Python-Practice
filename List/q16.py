#  Python program to find smallest number in a list

# Approach 1
l = [1, 2, 9, 3, 4, 56, 8, -1]
print(min(l))


# Approach 2
l = [1, 2, 9, 3, 4, 56, 8, -1, -100]
s = l[0]
for i in l:
    if s < i:
        pass
    else:
        s = i
print(s)

