n = int(input())

s = 0
while n > 0:
    d = n % 10
    n = n // 10
    s = s + d

print(s)
