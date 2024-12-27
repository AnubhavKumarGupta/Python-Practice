a = (input("Input the no. containing more than one digit's"))
total = 0
i = 0
while i < len(a):
    total += int(a[i])
    i += 1
print(total)
