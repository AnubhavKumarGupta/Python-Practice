#User function Template for python3


def minOperations(n):
    #Your code here
    if n == 1:
        return 0
    elif n % 2 == 0:
        return 1 + minOperations(n // 2)
    else:
        return 1 + min(minOperations(n - 1), minOperations(n + 1))