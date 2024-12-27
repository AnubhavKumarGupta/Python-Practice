n = [5, 3, 2, 2, 1, 5, 5, 7, 5, 10]
m = [10, 111, 1, 9, 5, 67, 2]


# for i in m:
#     count = 0
#     for j in n:
#         if i == j:
#             count += 1

#     print(count)




# d = [0] * 11
# for i in n:
#     d[i] += 1

# for i in m:
#     if i < 1 or i > 10:
#         print(0)
#     else:
#         print(d[i])




d = {}
for i in n:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

for i in m:
    if i in d:
        print(d[i])
    else:
        print(0)