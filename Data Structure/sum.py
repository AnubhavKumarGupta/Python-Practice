n = int(input())


def su(a):
    if a  <= 1:
        return a
    else:
        return a + su(a - 1)


print(su(n))


# def sum_of_natural_numbers(n):
#     if n <= 1:
#         return n
#     else:
#         return n + sum_of_natural_numbers(n - 1)

# # Example usage:
# n = 5  # You can change this value to any natural number
# result = sum_of_natural_numbers(n)
# print(f"The sum of the first {n} natural numbers is: {result}")
