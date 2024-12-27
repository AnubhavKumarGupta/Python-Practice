nums = [0, 3, 1]

n = []

s = []
for i in range(len(nums) + 1):
    n.append(i)

print(n)

for x in n:
    if x not in nums:
        s.append(x)
print(s)
