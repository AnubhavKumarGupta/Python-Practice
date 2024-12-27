# check number to be odd or even
a = int(input())
r = a % 2
is_even = (r == 0)
if is_even:
    print("a is even")
else:
    print("a is odd")
