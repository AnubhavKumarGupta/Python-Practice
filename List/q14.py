#  Python | Sum of number digits in List

# Approach 1
l = [12, 67, 98, 34]
sum = 0
for i in l:
    sum += i
print(sum)


# Approach 2
l = [12, 67, 98, 34]
print(sum(l))


# Approach 3
l = [12, 67, 98, 34]
sum = 0
for i in range(len(l)):
    sum += l[i]
print(sum)
