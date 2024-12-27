t = int(input())

for _ in range(t):
    a, b, c = map(int, input().split())
    d = a + c
    e = a + b
    f = b + c
    if d == b or e==c or f == a:
        print("yes")
    else:
        print("no")
