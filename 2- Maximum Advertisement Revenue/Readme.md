# Maximum Advertisement Revenue

## Explanation

The idea of this problem is that we want to place the highest profit-per-click ads on the slots with the highest average clicks-per-day, maximizing the total revenue. The goal is to multiply the maximum profit/click ad with the maximum clicks/day slot, then move on to the second-highest for both, and so on.

- **Naive algorithm**

  - Find the maximum of list `a` (profit per click) and the maximum of list `b` (clicks per day).
  - Multiply them and add to the total sum.
  - Remove these maximum values from both lists and repeat the process until the lists are empty.

- **Enhanced algorithm**

  - Sort both lists `a` and `b` and compute the dot product of these two sorted lists.
  - The sorting algorithm used is quicksort, which has a time complexity of O(log n).

## QUESTION

Calculate the Big-O of your algorithm for Maximum Advertisement Revenue:

- The complexity is **O(n + 2 log n) = O(n)**.

## Pseudo-code

```python
def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        great = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(great)

def max_dot_product_fast(a, b):
    res = 0
    a = quicksort(a)
    b = quicksort(b)
    for i in range(len(a)):
        res += a[i] * b[i]
    return res
```

## Stress Testing

```Python
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

```

Output:

```Terminal
Loading ...
Success
```
