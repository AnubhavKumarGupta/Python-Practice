# nums = [5,4,3,8]
# l1 = []
# l2 = []

# l1.append(nums[0])
# l2.append(nums[1])

# for i in range(len(nums)-2):
#     l1.append(nums[i])
#     l2.append(nums[i+1])
    
    
    
# l = l1 + l2
    
# print(l)


def distribute(nums):
    arr1 = [nums[1]]  # Start with the first number in arr1
    arr2 = []         # Start with an empty arr2
    is_last_to_arr1 = True  # Flag to track whether the last element was added to arr1
    for num in nums[2:]:
        if is_last_to_arr1:
            arr2.append(num)
        else:
            arr1.append(num)
        is_last_to_arr1 = not is_last_to_arr1  # Toggle the flag for the next iteration
    return arr1 + arr2  # Concatenate arr1 and arr2 to get the result

# Example usage:
nums = [2,1,3]
result = distribute(nums)
print(result)  # Output: [5, 3, 4, 8]
