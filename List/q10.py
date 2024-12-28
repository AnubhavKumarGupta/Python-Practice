#  Python | Cloning or Copying a list

# Approach 1:
l = [10, 20, 30, 40, 50]
l1 = l.copy()
print(l1)


# Approach 2:
l = [10, 20, 30, 40, 50]
l1 = l[:]
print(l1)


# Approach 3:
l = [10, 20, 30, 40, 50]
l1 = list(l)
print(l1)


# Approach 4:
l = [10, 20, 30, 40, 50]
l1 = []
for i in l:
    l1.append(i)
print(l1)


# Approach 5:
l = [10, 20, 30, 40, 50]
l1 = []
l1 = l
print(l1)



