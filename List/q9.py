# Python | Reversing a List


# Approach 1:
l = [10, 20, 30, 40, 50]
l.reverse()
print(l)


# Approach 2:   
l = [10, 20, 30, 40, 50]
print(l[::-1])


# Approach 3:
l = [10, 20, 30, 40, 50]
print(list(reversed(l)))


# Approach 4:
l = [10, 20, 30, 40, 50]
ll =[]
for i in l:
    ll.insert(0, i)
print(ll)


# Approach 5:
l = [10, 20, 30, 40, 50]
ll = []
for i in range(len(l)):
    ll.append(l.pop())
print(ll)