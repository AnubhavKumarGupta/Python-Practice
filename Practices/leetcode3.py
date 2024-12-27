class Solution:
    def getSmallestString(self, s: str, k: int) -> str:

    
        size = len(s)
        result = ""
        for i in range(size):
            action = min(ord(s[i]) - ord('a'), 26 - (ord(s[i]) - ord('a')))
            if k >= action:
                result += 'a'
                k -= action
            else:
                result += chr(ord(s[i]) - k)
                k = 0
        return result
