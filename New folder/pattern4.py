n = int(input())
row = 1
while row <= n:
    col = 1
    while col <= row:
        print(col, end="")
        col = col+1
    print()
    row = row+1
