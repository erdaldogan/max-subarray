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


def linear_time_max_subarray(array):
    max_so_far = 0
    max_ending_here = 0
    start, end = 0, 0
    for index in range(len(array)):
        max_ending_here = max_ending_here + array[index]
        if max_ending_here < array[index]:
            max_ending_here = array[index]
            start = index

        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
            end = index

    return array[start:end]


array = [-2, -5, 6, -20, -3, 1, 5, -6]
max_range = linear_time_max_subarray(array)
print(max_range)