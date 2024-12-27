def prefix_sum_in_place(arr):
    for i in range(1, len(arr)):
        arr[i] = arr[i] + arr[i - 1]
    return arr


# Example usage
arr = [1, 2, 3, 4, 5]
result = prefix_sum_in_place(arr)
print("Prefix sum array:", result)
