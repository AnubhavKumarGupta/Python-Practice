# a = (input("Input the no. containing more than one digit's"))
# total = 0
# temp = 0
# i = 0
# j = 0
# while i < len(a):
#     total += int(a[i])
#     i += 1
#     while j < total:
#         total += int(a[j])
#         i += 1
#     print(temp)

# a = (input("Input the no. containing more than one digit's"))
# total = 0
# i = 0
# while i < len(a):
#     total += int(a[i])
#     i += 1
# print(total)

# def sum(n):
#     if (n <= 9):
#         return n
#     return sum(n % 10 + n//10)


# sum(123)

a = (input("Input the no. containing more than one digit's"))
total = 0
i = 0
while i < len(a):
    total += int(a[i])
    i += 1
print(total)
