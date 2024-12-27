n = int(input())

l = input()

a = []
b = []

for i in l:
    if i == "A":
        a.append(i)
    else:
        b.append(i)


if len(a) > len(b):
    print("Anton")

elif len(a) < len(b):
    print("Danik")

else:
    print("Friendship")
