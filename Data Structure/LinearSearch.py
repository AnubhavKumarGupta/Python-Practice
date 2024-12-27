def linear(n, key):
    for i in range(len(n)):
        if key == n[i]:
            return i
    return -1


n = eval(input("Input the list\n"))
key = int(input(f"Which element you want to search "))
print(linear(n, key))
