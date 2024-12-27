
def countPairs(nums):
    # cnt = 0
    # s = 0
    # e = len(nums) - 1
    # while e > s:
    #     if str(nums(s)) == str(nums(e)[::-1]):
    #         cnt = cnt + 1
    #         s = s + 1
            
    #     else:
    #         break
    # return cnt
    
    cnt = 0
    
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if str(nums[i]) == str(nums[j])[::-1]:
                count = count + 1
            else:
                break

nums = [3,12,30,17,21]
print(countPairs(nums))