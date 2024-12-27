n = int(input("Enter a number: "))


def is_armstrong(n):
    original = n
    cnt = 0
    temp = n

    while temp != 0:
        temp = temp // 10
        cnt += 1

    temp = n
    armstrong_sum = 0

    while temp != 0:
        digit = temp % 10
        armstrong_sum += digit**cnt
        temp = temp // 10

    if armstrong_sum == original:
        print("Yes")
    else:
        print("NO")


is_armstrong(n)
