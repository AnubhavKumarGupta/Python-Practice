def can_partition_into_two_equal_sum_subarrays(arr):
    total_sum = sum(arr)

    # If total_sum is odd, it's not possible to partition it into two equal parts
    if total_sum % 2 != 0:
        return False

    left_sum = 0
    target_sum = total_sum // 2

    for num in arr:
        left_sum += num
        if left_sum == target_sum:
            return True

    return False


# Example usage
arr = [3, 4, -2, 5, 8, 20, -10, 8]
result = can_partition_into_two_equal_sum_subarrays(arr)
if result:
    print("The array can be partitioned into two equal sum subarrays.")
else:
    print("The array cannot be partitioned into two equal sum subarrays.")
