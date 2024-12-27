import string

s = input("Enter any string: ")
count = 0
for ch in s:
    if ch in string.ascii_uppercase:
        count += 1
print(f"Number of upper case characters in '{s}' is {count}")
