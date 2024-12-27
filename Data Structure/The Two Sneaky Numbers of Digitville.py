
def getSneakyNumbers(nums):
    l = []
    for i in nums:
        if i not in l:
            l.append(i)
    return l

nums = [0,3,2,1,3,2]

print(getSneakyNumbers(nums))