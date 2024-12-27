# import math

# class Solution:
    
#     def is_prime(self, n):
#         if n < 2:
#             return False
#         for i in range(2, int(math.sqrt(n)) + 1):
#             if n % i == 0:
#                 return False
#         return True

#     def maximumPrimeDifference(self, nums: List[int]) -> int:
#         md = 0
#         mp = -1
#         mp = -1

#         for i in range(len(nums)):
#             if self.is_prime(nums[i]):
#                 if mp == -1:
#                     mp = i
#                 mp = i

#         if mp != -1 and mp != -1:
#             md = mp - mp

#         return md
