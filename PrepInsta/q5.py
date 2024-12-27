a = int(input())
b = int(input())
c = int(input())


if a > b and a > c:
    print("Among all", a, "is the greatest")

elif b > a and b > c:
    print("Among all", b, "is the greatest")

else:
    print("Among all", c, "is the greatest")
