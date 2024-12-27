n = int(input())
row = 1
p = 1
while row <= n:
    col = 1
    while col <= row:
        print(p, end="")
        p = p+1
        col = col+1
    print()
    row = row+1
