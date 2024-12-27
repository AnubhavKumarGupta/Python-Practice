class Solution:
    
    def isUgly(self, n: int) -> bool:
        if n in [1, 2]:
            return True
        elif n % 2 == 0 and n % 3 == 0:
            return True
        else:
            return False
