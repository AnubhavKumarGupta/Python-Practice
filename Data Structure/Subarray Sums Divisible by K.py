def subarraysDivByK(nums, k):
    # count = 0
    for i in range(len(nums)):
        cs = 0
        for j in range(i, len(nums)):
            cs = cs + nums[j]
            if cs % k == 0:
                # count = count + 1
                print(nums[i : j + 1])


nums = [4, 5, 0, -2, -3, 1]
k = 5

subarraysDivByK(nums, k)
