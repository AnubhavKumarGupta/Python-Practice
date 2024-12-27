L = [1, 2, 3, 4, 5]
print(L)
# slice operation
d = int(input("Enter num of positions: "))
L = L[d:] + L[:d]
print(L)
