# Uses python3

import sys
import random

def max_dot_product_naive(a, b):
    # My code here
    res = 0

    for j in range(len(a)):
        # Initialize max variable for every loop
        max_a = None
        max_b = None

        for i in range(n - j):
            # Get max for list a
            if max_a == None or max_a < a[i]:
                max_a = a[i]

            # Get max for list b
            if max_b == None or max_b < b[i]:
                max_b = b[i]

        # Remove maxes so that not repeated en coming loops
        a.remove(max_a)
        b.remove(max_b)

        # Multiply maxes and sum with the result.
        res += max_a * max_b

    return res


def quicksort(array):
    if len(array) <= 1:  # Base Case : if array less than two elements
        return array
    else:
        # Choose the pivot
        pivot = array[0]

        # Make list of less items than pivot
        less = [item for item in array[1:] if item <= pivot]

        # Make list of great items than pivot
        great = [item for item in array[1:] if item > pivot]

        # put items less than pivot in the left and put items great than pivot in the right
        # Recursion : repeat and sort the smaller lists
        return quicksort(less) + [pivot] + quicksort(great)


def max_dot_product_fast(a, b):
    res = 0

    # Sort a and b list
    a = quicksort(a)
    b = quicksort(b)

    # Sum of Multiple of 2 lists
    for i in range(len(a)):
        res += a[i] * b[i]
    return res


if __name__ == "__main__":

    """Stress Testing"""
    i = 0
    print("Loading ...")
    while i < 1000:
        a = list()
        b = list()
        n = random.randint(1, 10 ** 3)
        for i in range(n):
            a.append(random.randint(-(10 ** 5), 10 ** 5))
            b.append(random.randint(-(10 ** 5), 10 ** 5))

        if max_dot_product_fast(a, b) != max_dot_product_naive(a, b):
            print(n)
            print(a)
            print(b)

            print("Field !")
            break

        i += 1

    if i == 1000:
        print("Success")

    # input = sys.stdin.read()
    # data = list(map(int, input.split()))
    # n = data[0]
    # a = data[1 : (n + 1)]
    # b = data[(n + 1) :]
    # print(max_dot_product_fast(a, b))
