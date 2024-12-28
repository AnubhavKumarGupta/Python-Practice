# Python Program to find sum and average of List in Python

# Approach 1
l = [1, 2, 3, 4, 5]
print(sum(l))
print(sum(l) / len(l))


# Approach 2
l = [1, 2, 3, 4, 5]
sum = 0
for i in l:
    sum += i
print(sum)
print(sum / len(l))


# Approach 3
l = [1, 2, 3, 4, 5]
sum = 0
for i in range(len(l)):
    sum += l[i]
print(sum)
print(sum / len(l))
