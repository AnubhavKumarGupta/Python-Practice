def print_even(n):
    if n <= 0:
        return
    if n % 2 == 0:
        print_even(n - 2)
        print(n)
    else:
        print_even(n - 1)

# Taking user input
num = int(input("Enter a number: "))
print_even(num)
