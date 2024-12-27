class Solution:
    def minimumLevels(self, possible: List[int]) -> int:
        n = len(possible)
        p = [0] * n
        
        if possible[0] == 0:
            possible[0] = -1
        p[0] = possible[0]
        
        for i in range(1, n):
            if possible[i] == 0:
                possible[i] = -1
            p[i] = possible[i] + p[i - 1]
        
        for i in range(n - 1):
            s1 = p[i]
            s2 = p[n - 1] - p[i]
            if s1 > s2:
                return i + 1
        
        return -1
