t = int(input())
for _ in range(t):
    a = input()
    b = len(a)
    if b <= 10:
        print(a)
    else:
        print(a[0] + str(len(a) - 2) + a[-1])



#Done