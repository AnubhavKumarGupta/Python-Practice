def suffix_sum_in_place(arr):
    for i in range(len(arr) - 2, -1, -1):
        arr[i] += arr[i + 1]
    return arr

# Example usage
arr = [1, 2, 3, 4, 5]
result = suffix_sum_in_place(arr)
print("Suffix sum array (in-place):", result)
