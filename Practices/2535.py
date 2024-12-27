# class Solution:
#     def minimumAverage(self, nums: List[int]) -> float:
#         nums.sort()
#         a = []
#         while len(nums) > 0:
#             me = nums.pop(0)
#             ma = nums.pop(-1)
#             avg = (me + ma) / 2
#             a.append(avg)
#         return round(min(a), 1)
