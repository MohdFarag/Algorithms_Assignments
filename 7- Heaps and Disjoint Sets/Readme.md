# Heaps and Disjoint Sets

## Heap

### Explanation

By looping on elements of a given array, we will use Heapify(A, i, swaps) algorithm which is process used to create Min-Heap.

- Find the smallest between childs of given node and a given node.
- Swap between the smallest and given node.
- Add pairs of swapping to swaps array.
- Heapify the root.

### Pseudocode

```Python
minHeapify(array, i, swaps)
  leftChild = leftChild of i
  rightChild = rightChild of i

  if array[leftChild] < array[smallest]
    set leftChild as smallest
  else
    set smallest as i

  if array[rightChild] < array[smallest]
    set rightChild as smallest

  if smallest not equal i
    swap array[i] and array[smallest]
    Append (i, smallest) to swaps
    minHeapify(array, smallest, swaps)

build_heap(array)
  swaps = []
  loop i from the first index down to zero
     min_Heapify(Array, i, swaps)
```

---

## Heapsort

### Explanation

First : build max Heap using max Heapify
Second : loop n times

- Swap array[n] and array[0]
- n = n-1
- Heapify the root

### Pseudocode

```Python
heap_sort(arr)
	Build_max_Heap()
	Loop n times :
		Swap(arr[n],arr[0])
		set n as n-1
		Heapify(arr, n, 0)
```

---

## Disjoint

### Explanation

- Get the parent(symbolic links) of given source and destination table.
	- Traverse the path of symbolic links to get to the data.
    𝑑𝑒𝑠𝑡𝑖𝑛𝑎𝑡𝑖𝑜𝑛𝑖 <- symlink(𝑑𝑒𝑠𝑡𝑖𝑛𝑎𝑡𝑖𝑜𝑛𝑖)

- If d𝑒𝑠𝑡𝑖𝑛𝑎𝑡𝑖𝑜𝑛𝑖 ≠ 𝑠𝑜𝑢𝑟𝑐𝑒, compare by rank of source and destination table.
	- copy data from lower rank to upper rank.

- Clear the source table.

- Update max row count with the new maximum table size.

### Pseudocode

```Python
get_parent(table):
    initialize parents_Update => empty list

    set root => table
    while root not equal parents[root]
    	Add parents[root] to parents_Update
        set root => self.parents[root]

    loop items i in parents_Update
    	set parents[i] => root

    return root


merge(src, dst):
       set src_parent => get_parent(src)
       set dst_parent => get_parent(dst)

       if src_parent = dst_parent:
            return False

       if ranks[src_parent] more than ranks[dst_parent]:
            set parents[src_parent] => dst_parent
       else
            set parents[dst_parent] => src_parent
            if ranks[src_parent] = ranks[dst_parent]:
                increment ranks[src_parent] by 1

       row_counts[dst_parent] => row_counts[dst_parent] + row_counts[src_parent]
       set row_counts[src_parent] => zero

       if max_row_count less than row_counts[dst_parent] :
          set max_row_count => row_counts[dst_parent]

       return True
```

### References

-	https://www.educative.io/edpresso/how-to-build-a-heap-from-an-array

-	https://favtutor.com/blogs/heap-in-python

-	https://www.geeksforgeeks.org/heap-sort/

-	Course 2 — Data structure — Part 2: Priority queues and Disjoint set | by Phat Le | Towards Data Science
