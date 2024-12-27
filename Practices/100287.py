def minimumAddedInteger(nums1, nums2):
    nums1.sort()
    nums2.sort()
    return nums2[-1] - nums1[-1]


nums1 = [4,20,16,12,8]
nums2 = [14,18,10]
print(minimumAddedInteger(nums1, nums2))