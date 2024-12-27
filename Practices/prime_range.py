arrstart = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))
l = []


def f(i):
    if i == 1:
        return 0
    for j in range(2, int(i**0.5) + 1):
        if (i % j) == 0:
            return 0
    return 1


for i in range(start, end + 1):
    # if i > 1:
    #     for j in range(2, int(i**0.5) + 1):
    #         if (i % j) == 0:
    #             break
    #     else:
    if f(i) == 1:
        l.append(i)

print(l)
print(l.count(i))


# a = "".join(l)
# print(a)
# def f(i):
#     for j in range(2, int(i**0.5) + 1):
#         if (i % j) == 0:
#             return 0
#     return 1
