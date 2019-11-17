import random


def brute_force_max_subarray(array):
    length = len(array)
    max_sum_index = (0, 0, 0)
    max_sum = 0
    for start in range(length):
        sum = 0
        for end in range(start, length):
            sum += array[end]
            if sum > max_sum:
                max_sum = sum
                max_sum_index = (max_sum, start, end)
    return max_sum_index


def linear_time_max_subarray(array):
    max_so_far = -10000
    max_ending_here = -10000
    start, end = 0, 0
    for index in range(len(array)):
        max_ending_here = max(array[index], max_ending_here + array[index])
        if max_ending_here == array[index]:
            start = index

        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
            end = index
            final_start = start

    return max_so_far, final_start, end


def max_crossing_subarray(array, l, m, h):
    left_max_sum = -1000000
    sum_l = 0
    left_start_index = 0
    for i in range(m, l - 1, -1):
        sum_l = sum_l + array[i]
        if sum_l > left_max_sum:
            left_max_sum = sum_l
            left_start_index = i

    right_end_index = 0
    sum_r = 0
    right_max_sum = -100000
    for j in range(m + 1, h + 1):
        sum_r = sum_r + array[j]
        if sum_r > right_max_sum:
            right_max_sum = sum_r
            right_end_index = j

    return left_max_sum + right_max_sum, left_start_index, right_end_index


def divide_and_conquer_max_subarray(array, l, h):
    m = int((h + l) / 2)

    if l == h:
        return array[l], l

    return max(
        max_subarray(array, l, m),
        max_subarray(array, m + 1, h),
        max_crossing_subarray(array, l, m, h)
    )

def generate_random_array(number):
    output = []
    for i in range(number):
        output.append(random.randint(-100,100))
    return output


#array = [-2, -5, 6, -2, -3, 1, 5, -6]
array = [-2, 7, 6, -4, -2, -3, -1, -5, -6]
random_array = generate_random_array(100)
max_range = max_subarray(random_array, 0, len(random_array) - 1)
max_range1 = linear_time_max_subarray(random_array)
max_range2 = brute_force_max_subarray(random_array)

def runningTimeComparison():
    n_variations = [10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000]

    # for setting the bounds of numbers for the randomly created array
    array_num_lower_bound, array_num_upper_bound = -10000, 10000
    # for storing the time elapsed while running the algorithm
    linear_time_arr, brute_time_arr, divide_and_conquer_max_subarray_time_arr = [], [], []

    for n in n_variations:
        array = []
        for _ in range(n):
            array.append(random.randint(array_num_lower_bound, array_num_upper_bound))

        start = time.time()
        print("divide_and_conquer_max_subarray", n)
        max_output = divide_and_conquer_max_subarray(array, 0, len(array) - 1)
        end = time.time()
        divide_and_conquer_max_subarray_time_arr.append(end - start)

        start = time.time()
        print("linear_time_max_subarray", n)
        linear_output = linear_time_max_subarray(array)
        end = time.time()
        linear_time_arr.append(end - start)

        start = time.time()
        print("brute_force_max_subarray", n)
        brute_output = brute_force_max_subarray(array)
        end = time.time()
        brute_time_arr.append(end - start)

    print("divide_and_conquer_max_subarray_time_arr", divide_and_conquer_max_subarray_time_arr)
    print("linear_time_arr", linear_time_arr)
    print("brute_time_arr", brute_time_arr)


def maximumSubarray(array):
    print("***********************")
    start = time.time()
    print("divide_and_conquer_max_subarray")
    max_output = divide_and_conquer_max_subarray(array, 0, len(array) - 1)
    end = time.time()
    print("Max Sum:\t\t" + str(max_output[0]))
    print("Indices:\t\t" + str(max_output[1]) + "-" + str(max_output[2]))
    print("Time Elapsed:\t" + str(end - start) + "s")

    print("***********************")
    start = time.time()
    print("linear_time_max_subarray")
    linear_output = linear_time_max_subarray(array)
    end = time.time()
    print("Max Sum:\t\t" + str(linear_output[0]))
    print("Indices:\t\t" + str(linear_output[1]) + "-" + str(linear_output[2]))
    print("Time Elapsed:\t" + str(end - start) + "s")

    print("***********************")
    start = time.time()
    print("brute_force_max_subarray")
    brute_output = brute_force_max_subarray(array)
    end = time.time()
    print("Max Sum:\t\t" + str(brute_output[0]))
    print("Indices:\t\t" + str(brute_output[1]) + "-" + str(brute_output[2]))
    print("Time Elapsed\t: " + str(end - start) + "s")
    print("***********************")





a1 = [-2, -5, 6, -2, -3, 1, 5, -6]
a3 = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]

print("ARRAY 1")
maximumSubarray(a1)

print("ARRAY 3")
maximumSubarray(a3)
