# Uses python3
import sys
import random


"""Naive Approach"""
def get_number_of_inversions_naive(a, n):

    number_of_inversions = 0

    for i in range(n):
        for j in range(i, n):
            if (a[i] > a[j]):
                number_of_inversions += 1

    return number_of_inversions


"""Using merge sort"""
def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0
    if right - left <= 1:
        return number_of_inversions
    ave = (left + right) // 2
    number_of_inversions += get_number_of_inversions(a, b, left, ave)
    number_of_inversions += get_number_of_inversions(a, b, ave, right)

    sorted_array, num = Merge(a[left: ave], a[ave: right])

    a[left:right] = sorted_array
    number_of_inversions += num

    return number_of_inversions

def Merge(a, b):
    c = []
    i = 0
    j = 0
    numOfInversions = 0
    while i < len(a):
        if j == len(b):
            c += a[i:]
            break

        if a[i] == b[j]:
            c.append(a[i])
            i += 1

        elif a[i] > b[j]:
            c.append(b[j])
            numOfInversions += (len(a) - i)
            j += 1
        else:
            c.append(a[i])
            i += 1
    if j < len(b):
        c += b[j:]

    return c, numOfInversions


if __name__ == '__main__':
    # DO NOT change this code
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(get_number_of_inversions(a, b, 0, len(a)))

    """Stress Testing"""
    # while True:
    #     n = random.randint(1,10**5)
    #     a = [random.randint(1,10**9) for i in range(n)]
    #     b = n * [0]
    #     if get_number_of_inversions_naive(a, n) == get_number_of_inversions(a, b, 0, len(a)):
    #         print(True)
    #     else :
    #         print(False)
    #         break
