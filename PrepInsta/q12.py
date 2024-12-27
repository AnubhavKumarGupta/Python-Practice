n =int(input())

s = str(n)

if s == s[::-1]:
    print("It is Palindrome")
else:
    print("It is not Palindrome")