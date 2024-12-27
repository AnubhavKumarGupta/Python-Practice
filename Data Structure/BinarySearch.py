def bsh(n, key):
    low = 0
    high = len(n) - 1
    while low <= high:
        mid = (low + high) // 2
        if key == n[mid]:
            return mid
        elif key < n[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return -1

n = eval(input())
key = int(input())
n.sort()
print(bsh(n, key))
