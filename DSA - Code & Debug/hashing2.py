# s = "azyxyyzaaaa"
# q = ["d", "a", "y", "x"]

# d = [0] * 26

# for i in s:
#     ascii_value = ord(i)
#     index = ascii_value - 97
#     d[index] += 1


# for i in q:
#     ascii_value = ord(i)
#     index = ascii_value - 97
#     print(d[index])

# s = "azyxyyzaaaa"
# q = ["d", "a", "y", "x"]

# d = {}

# for i in s:
#     if i in d:
#         d[i] += 1
#     else:
#         d[i] = 1

# for i in q:
#     if i in d:
#         print(d[i])
#     else:
#         print(0)



s = "aZyXyyzaAAA"
q = ["d", "a", "y", "x", "A", "Z"]

d = {}

for i in s:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

for i in q:
    if i in d:
        print(d[i])
    else:
        print(0)