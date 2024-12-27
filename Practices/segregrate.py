n = [1, 0, 1, 0, 0, 1,0]

count0 = 0
count1 = 0

for i in n:
    if n[i] == 0:
        count0 += 1
    else:
        count1 += 1

for i in range(count0):
    n[i] = 0

for i in range(count1, len(n)):
    n[i] = 1

print(n)
