# Python– Avoid Spaces in string length


# Approach 1 : Using replace function
n = input("Enter the string: ")
print(n.replace(" ", ""))


# Approach 2 : Using for loop
n = input("Enter the string: ")
count = 0
for i in n:
    if i != " ":
        count += 1
print(count)


