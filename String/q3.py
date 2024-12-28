# Ways to remove i’th character from string in Python

# Approach 1 - Using Python String slicing
n = input("Enter the string: ")
i = int(input("Enter the index: "))
print(n[:i] + n[i + 1 :])



# Approach 2 - Using Python For loop
n = input("Enter the string: ")
i = int(input("Enter the index: "))
s = ""
for j in range(len(n)):
    if j != i:
        s = s + n[j]
print(s)


# Approach 3 - Using remove function
n = input("Enter the string: ")
i = int(input("Enter the index: "))
print(n.replace(n[i], ""))
