
def numSubarrayProductLessThanK(nums,k):
    for i in range(len(nums)):
        cs = 1
        for j in range(i,len(nums)):
            cs = cs * nums[j]
            if cs < k:
                print(nums[i:j+1])


nums = [10,5,2,6]
k = 100
numSubarrayProductLessThanK(nums,k)
