def largest_sum_contiguous_subarray(arr):
    max_so_far = float("-inf")
    max_ending_here = 0

    for num in arr:
        max_ending_here += num
        if max_ending_here < num:
            max_ending_here = num
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here

    return max_so_far


# Example usage
arr = [3, 4, -5, 8, -12, 7, 6, -2]
print("The largest sum contiguous subarray is:", largest_sum_contiguous_subarray(arr))
