# Python program to check whether the string is Symmetrical or Palindrome

# Approach 1 - Using Python String slicing
# n = input("Enter the string: ")
# if n == n[::-1]:
#     print("The string is Palindrome")
# else:
#     print("The string is not Palindrome")



# Approach 2 - Using Python While loop and two pointers (left and right) 
# n = input("Enter the string: ")
# s = n
# l = 0
# r = len(n) - 1

# is_palindrome = True

# while l < r:
#     if s[l] != s[r]:
#         is_palindrome = False
#         break
#     l += 1
#     r -= 1

# if is_palindrome:
#     print("Palindrome")
# else:
#     print("Not Palindrome")


# Approach 3 - Using Python For loop 
n = input("Enter the string: ")

s = ""
for i in n:
    s = i + s
    
if n == s:
    print("Palindrome")
else:
    print("Not Palindrome")
    
