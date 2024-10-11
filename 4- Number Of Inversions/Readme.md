# Number of Inversions

## I. Naive Approach (without using merge sort)

### Explanation

Traverse through the array, and for every index, find the number of smaller elements on its right side of the array.

### Pseudo-code

```Pseudo
Def get_number_of_inversions_naive(A, n):
1   SET number_of_inversions = 0
2   for i from 0 to n:
3       for j from i to n:
4           number_of_inversions += 1
5   return number_of_inversions
```

---

## II. Enhanced approach (using merge sort)

### Explanation

For each array element, count all elements more than it to its left and add the count to the output. This already happens inside the merge function of merge sort.

### Pseudo-code

```Pseudo
Def get_number_of_inversions (a, b, left, right):
1   number_of_inversions = 0
2   if right <= left:
3       return number_of_inversions
4
5   ave = (left + right) / 2
6   number_of_inversions += get_number_of_inversions(a, b, left, ave)
7   number_of_inversions += get_number_of_inversions(a, b, ave + 1, right)
8   number_of_inversions += merge(a, b, left, ave, right)
9
10  sorted_array, num = Merge(a[left: ave], a[ave: right])
11
12  a[left:right] = sorted_array
13  number_of_inversions += num
14  return number_of_inversions
```

```Pseudo
Def merge (a, b):

1   set c empty list
2   i = 0
3   j = 0
4   numOfInversions = 0
5
6   while i < length of a:
7       if j = length of b:
8           c += a[i:]
9           break
10
11      if a[i] = b[j]:
12          append a[i] to c
13          i += 1
14
15      elif a[i] > b[j]:
16          append b[i] to c
17          numOfInversions += len(a) - i
18          j += 1
19      else:
20          append a[i] to c
21          i += 1
22
23  if j < len(b):
24      c += b[j:]
25
26  return (c, numOfInversions)


```

## References

I. Count Inversions in an array | Set 1 (Using Merge Sort) - GeeksforGeeks
II. Inversion count of an array - Techie Delight
