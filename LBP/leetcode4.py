# class Solution:
#     def countAlternatingSubarrays(self, nums: List[int]) -> int:
#         cnt = 0
#         l = 1
        
#         for i in range(len(nums)):
#             if i > 0 and nums[i] != nums[i - 1]:
#                 l += 1
#             else:
#                 l = 1
#             cnt += l
        
#         return cnt
