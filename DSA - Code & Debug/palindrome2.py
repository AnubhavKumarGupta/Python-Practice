n = int(input("Enter a number: "))
on = n

s = 0
while n > 0:
    d = n % 10
    s = s * 10 + d
    n = n // 10

# print(s)

if on == s:
    print("Yes")
else:
    print("No")
