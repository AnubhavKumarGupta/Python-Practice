def pal(a):
    if a == a[::-1]:
        return "Yes"
    else:
        return "No"


n = int(input())

print(pal(str(n)))
