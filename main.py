import random
import time

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
    max_so_far = -10000
    max_ending_here = -10000
    start, end = 0, 0
    for index in range(len(array)):
        max_ending_here = max_ending_here + array[index]
        if max_ending_here < array[index] and array[index] >= max_so_far:
            max_ending_here = array[index]
            start = index

        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
            end = index

    return max_so_far, start, end


def max_crossing_subarray(array, l, m, h):
    left_max_sum = -1000000
    sum_l = 0
    for i in range(m, l - 1, -1):
        sum_l = sum_l + array[i]
        if sum_l > left_max_sum:
            left_max_sum = sum_l

    sum_r = 0
    right_max_sum = -100000
    for j in range(m + 1, h + 1):
        sum_r = sum_r + array[j]
        if sum_r > right_max_sum:
            right_max_sum = sum_r

    return left_max_sum + right_max_sum

def divide_and_conquer_max_subarray(array, l, h):
    m = int ((h + l) / 2)

    if l == h:
        return array[l]

    return max(
        divide_and_conquer_max_subarray(array, l, m),
        divide_and_conquer_max_subarray(array, m + 1, h),
        max_crossing_subarray(array, l, m, h)
    )


array_num_lower_bound = -10000
array_num_upper_bound = 10000
linear_time_arr=[]
brute_time_arr=[]
divide_and_conquer_max_subarray_time_arr=[]

n_variations = [10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000]
for n in n_variations:
    array = []
    for _ in range(n):
        array.append(random.randint(array_num_lower_bound,array_num_upper_bound))

    start=time.time()
    print("divide_and_conquer_max_subarray", n)
    max_output = divide_and_conquer_max_subarray(array, 0, len(array) - 1)
    end=time.time()
    divide_and_conquer_max_subarray_time_arr.append(end - start)

    start=time.time()
    print("linear_time_max_subarray", n)
    linear_output = linear_time_max_subarray(array)
    end = time.time()
    linear_time_arr.append(end - start)

    start=time.time()
    print("brute_force_max_subarray", n)
    brute_output = brute_force_max_subarray(array)
    end = time.time()
    brute_time_arr.append(end - start)

print("divide_and_conquer_max_subarray_time_arr", divide_and_conquer_max_subarray_time_arr)
print("linear_time_arr", linear_time_arr)
print("brute_time_arr", brute_time_arr)