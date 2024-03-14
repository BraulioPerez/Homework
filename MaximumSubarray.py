import random


def MaxSubarray(array):
    n = len(array)
    max_sum = -100000000000
    # Kadane's algorithm

    for i in range(0,n):
        curr_sum = 0
        for j in range(i, n):
            curr_sum = curr_sum + array[j]
            if (curr_sum > max_sum):
                max_sum = curr_sum
    print(f"the list was {len(array)}")
    print(f"the max sum was {max_sum}")
    return max_sum

def main():
    MaxSubarray([random.randint(-1000000, 1000000) for _ in range(10000)])

if __name__ == "__main__":
    main()