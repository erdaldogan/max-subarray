def brute_force_max_subarray(array):
    length = len(array)
    max_sum_index = (0, 0)
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
    max_so_far = array[0]
    max_ending_here = array[0]
    start, end = 0, 0
    for index in range(1, len(array)):
        max_ending_here=max(max_ending_here, max_ending_here+array[index])
        if max_ending_here==array[index]:
            start = index

        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
            end = index


    return max_so_far,start, end


def max_crossing_subarray(array, l, m, h):
    left_max_sum = -99999
    sum_l = 0
    left_start_index = 0
    for i in range(m, l - 1, -1):
        sum_l = sum_l + array[i]
        if sum_l > left_max_sum:
            left_max_sum = sum_l
            left_start_index=i

    right_end_index = 0
    sum_r = 0
    right_max_sum = -99999
    for j in range(m + 1, h+1):
        sum_r = sum_r + array[j]
        if sum_r > right_max_sum:
            right_max_sum = sum_r
            right_end_index=j

    return left_max_sum + right_max_sum, left_start_index, right_end_index


def max_subarray(array, l, h):
    m = int((h + l) / 2)

    if l == h:
        return array[l], l

    return max(max_subarray(array, l, m),max_subarray(array, m + 1, h),max_crossing_subarray(array, l, m, h))


array = [-2, 7, 6, -4, -2, -3, -1, -5, -6]
brute = brute_force_max_subarray(array)
linear = linear_time_max_subarray(array)
max_range = max_subarray(array, 0, len(array) - 1)
print(max_range)
print(linear)
print(brute)
