arr1 = [14, 20, 16, 88]
arr2 = [77, 65, 43, 63, 78]

k = int(input("Enter the kth element which you need "))
l = arr1 + arr2

l.sort()
print(l[k])

