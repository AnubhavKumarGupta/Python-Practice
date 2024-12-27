def search(b, a):
    if a in l:
        return True
    else:
        return False


l = list(map(int, input().split()))
n = int(input())
x = search(l, n)
if x == True:
    print("Found")
else:
    print("Not found")
