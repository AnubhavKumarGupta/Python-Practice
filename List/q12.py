#  Python | Count occurrences of an element in a list

# Approach 1
l = [1, 1, 1, 2, 2, 3, 4, 5, 5, 5, 5, 5]
print(l.count(5))


# Approach 2
l = [1, 1, 1, 2, 2, 3, 4, 5, 5, 5, 5, 5]
count = 0
for i in l:
    if i == 5:
        count += 1
print(count)
