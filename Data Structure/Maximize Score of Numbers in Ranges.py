from typing import List

def maxPossibleScore(start: List[int], d: int) -> int:
    start.sort()
    l, h = 0, d
    
    def fun(m: int) -> bool:
        p = start[0]
        for i in range(1, len(start)):
            if p + m > start[i] + d:
                return False
            p = max(start[i], p + m)
        return True

    while l < h:
        m = (h + l + 1) // 2
        if fun(m):
            l = m
        else:
            h = m - 1

    return l

start = [6,0,3]
d = 2
print(maxPossibleScore(start, d))  # Output: 5
