# Reverse words in a given String in Python

# Approach 1 
n = input("Enter the string: ")
print(n[::-1])



# Approach 2 
n = input("Enter the string: ")
s = ""
for i in n:
    s = i + s
print(s)

