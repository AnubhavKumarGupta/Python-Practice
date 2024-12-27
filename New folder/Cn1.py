
a = int(input())

while a != 6:

    if a <= 5 and a >= 1:

        b = int(input())

        c = int(input())

    if a == 1:
        print(b+c)

    if a == 2:
        print(b-c)

    if a == 3:
        print(b*c)

    if a == 4:
        print(b//c)

    if a == 5:
        print(b % c)

    elif a < 1 or a > 6:
        print("Invalid Operation")

    a = int(input())
