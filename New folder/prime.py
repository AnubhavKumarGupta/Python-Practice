# a = int(input())
# d = 2
# flag = False

# while(d < a):
#     if(a % d == 0):
#         flag = True
#     d = d+1
# if flag:
#     print("Not Prime")
# else:
#     print("Prime")

import random
import string

def generate_password(length=8, include_digits=True, include_symbols=True):
    chars = string.ascii_letters
    if include_digits:
        chars += string.digits
    if include_symbols:
        chars += string.punctuation
    password = ""
    for i in range(length):
        password += random.choice(chars)
    return password

length = int(input("Enter length of password: "))
include_digits = input("Include digits? (y
