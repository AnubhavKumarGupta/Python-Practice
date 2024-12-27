n = int(input())


s = str(n)

if n == int(s[::-1]):
    print("Yes")
else:
    print("No")
