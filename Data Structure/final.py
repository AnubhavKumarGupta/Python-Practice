def perform_operations(nums, k, multiplier):
    MOD = 10**9 + 7  # Modulo value

    while k > 0:
        # Find the index of the first minimum value in the list
        min_index = nums.index(min(nums))
        # Replace the selected minimum value with x * multiplier
        nums[min_index] *= multiplier
        # Decrease the number of operations
        k -= 1
    
    # Apply modulo 10^9 + 7 to each value in nums
    nums = [x % MOD for x in nums]

    return nums

# Example usage:
nums1 = [2,1,3,5,6]
k1 = 5
multiplier1 = 2
print(perform_operations(nums1, k1, multiplier1))  # Output: [8, 4, 6, 5, 6]

nums2 = [100000, 2000]
k2 = 2
multiplier2 = 1000000
print(perform_operations(nums2, k2, multiplier2))  # Output: [999999307, 999999993]
