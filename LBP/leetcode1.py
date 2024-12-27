# class Solution:
#     def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
#         ml = 51  
#         if k == 0:
#             return 1
#         for i in range(len(nums)):
#             r = 0
#             l = 0 
#             j = i
#             while j < len(nums) and k > r:
#                 r |= nums[j]
#                 l += 1  
#                 j += 1
#             if k <= r:
#                 ml = min(ml, l)  
#         return ml if ml != 51 else -1