def brute_force_max_subarray(array):
    length = len(array)
    max_sum_index= (0,0)
    max_sum = 0
    for start in range(length):
        sum = 0
        for end in range(start, length):
            sum += array[end]
            if sum > max_sum:
                max_sum = sum
                max_sum_index = (start, end)
    return max_sum_index



array = [-2, -5, 6, -2, -3, 1, 5, -6]
max_range = brute_force_max_subarray(array)
print(max_range)
