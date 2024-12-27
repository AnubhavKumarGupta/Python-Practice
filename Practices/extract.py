def fun(n):
    count = 0
    while n != 0:
        d = n % 10
        count = count + 1
        n = n // 10
    return count


n = int(input("Enter any number: "))
print(f"Number: {n} and number of digits: {fun(n)}")
