# Python | Ways to check if element exists in list


# Approach 1:
l = [10, 20, 30, 40, 50]
if 20 in l:
    print("Yes")
else:
    print("No")
    
    
# Approach 2:
l = [10, 20, 30, 40, 50]
for i in l:
    if i == 20:
        print("Yes")
        break
else:
    print("No")
    