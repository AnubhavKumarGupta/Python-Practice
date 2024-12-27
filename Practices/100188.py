# class Solution:
#     def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
#         result = [0] * n  
#         for i in range(1, n + 1):
#             for j in range(1, n + 1):

#                 m = min(abs(i - j), 1 + abs(i - x) + abs(j - y), 1 + abs(i - y) + abs(j - x))
            
#                 if m != 0:  
#                     result[m - 1] += 1
    
#         return result
