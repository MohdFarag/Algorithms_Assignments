# Uses python3
import sys
import random


def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m


def get_fibonacci_huge_fast(n, m):

    # Initialize variables
    previous = 0
    current = 1

    mod_current = -1

    # Initialize the list that contains pisano period
    pisano_period = []

    # The loop will stop if the pisano period has 0 and 1 in the period.
    while pisano_period[-2:] != [0, 1]:

        # Start Fibonacci sequence to compute.
        previous, current = current, previous + current

        # Take each number in Fibonacci mod (%) m to fill pisano period.
        mod_current = current % m
        pisano_period.append(mod_current)

    # The loop will stop with [0,1] in the end so move to the start of the list.
    pisano_period = pisano_period[-2:] + pisano_period[:-2]

    # Compute Fibonacci sequence until (n mod length of pisano period)
    previous = 0
    current = 1
    n %= len(pisano_period)
    for _ in range(n):
        previous, current = current, previous + current

    return previous % m


if __name__ == "__main__":

    """Stress Testing"""
    # while True:
    #     n = random.randint(1, 10 ** 5) # until 10**5
    #     m = random.randint(2, 10 ** 3)
    #     print(n, m)
    #     if get_fibonacci_huge_naive(n, m) != get_fibonacci_huge_fast(n, m):
    #         print("Wrong !")
    #         break
    #     else:
    #         print("Ok")

    input = sys.stdin.read()
    n, m = map(int, input.split())
    print(get_fibonacci_huge_fast(n, m))
