import random


def MaxSubarray(array):
    n = len(array)
    max_sum = -100000000000
    # Kadane's algorithm

    for i in range(0,n):
        curr_sum = 0
        for j in range(i, n):
            curr_sum = curr_sum + array[j]
            print(f"current sum = {curr_sum}")
            if (curr_sum > max_sum):
                max_sum = curr_sum
                print(f"max sum = {max_sum}")
    print(f"the list was {array}")
    print(f"the max sum was {max_sum}")
    return max_sum

MaxSubarray([random.randint(-1000000, 1000000) for _ in range(random.randint(0, 100))])