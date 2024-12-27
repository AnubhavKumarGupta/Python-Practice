# a = input()
# temp = ""
# i = 0
# while i < len(a):
#     if a[i] not in temp:
#         temp += a[i]

#     print(f"{a[i]} : {a.count(a[i])}")
#     i += 1

a = input()
temp = ""
for i in range(len(a)):
    if a[i] not in temp:
        print(f"{a[i]} : {a.count(a[i])}")
    temp += a[i]
    i += 1
