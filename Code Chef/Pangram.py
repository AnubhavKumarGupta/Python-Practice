n = int(input())
s = input()

print(s.lower())

S = set(s)

if len(S) == 26:
    print("YES")

else:
    print("NO")
