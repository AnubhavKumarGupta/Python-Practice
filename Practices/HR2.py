def plusMinus(arr):
    # Write your code here
    p = []
    n = []
    z = []
    for i in arr:
        if i < 0:
            n.append(i)

        elif i == 0:
            z.append(i)

        else:
            n.append(p)

    print(len(p) // len(arr))
    return len(z) // len(arr)
    return len(n) // len(arr)


plusMinus([-4, 3, -9, 0, 4, 1])
