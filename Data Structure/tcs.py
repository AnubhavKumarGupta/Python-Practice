def find_subarrays_brute_force(nums, target_sum):
    for i in range(len(nums)):
        current_sum = 0
        for j in range(i, len(nums)):
            current_sum += nums[j]
            if current_sum == target_sum:
                print(nums[i:j+1])

nums = [3, 4, -7, 1, 3, 3, 1, -4]
k = 7
find_subarrays_brute_force(nums, k)  # Removed the print statement here
