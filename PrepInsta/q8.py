a = int(input())
b = int(input())

def pr(a, b):
    l = []
    for i in range(a, b + 1):
        if i > 1:
            for j in range(2, int(i**0.5) + 1):
                if i % j == 0:
                    break
            else:
                l.append(i)
    # return l
    return sum(l)


print(pr(a,b))


# print(pr(a, b))
