# python3
import random

# return left child
def leftChild(i):
    return 2 * i + 1

# return right child
def rightChild(i):
    return 2 * i + 2

def min_heapify(A,i,swaps):
    left = leftChild(i) # return left child of givin index
    right = rightChild(i) # return right child of givin index

    ### Find the index of smallest value between given index, left and right
    
    if left < len(A) and A[left] < A[i]: # smallest = index of min(A[left],A[i])
    # if given index has a left child 
    # AND left child value less than given index value  
        smallest = left
    else:
        smallest = i

    if right < len(A) and A[right] < A[smallest]: # smallest = index of min(A[right],A[smallest])
    # if given index has a right child 
    # AND right child value less than smallest index value  
        smallest = right

    # If there is a child less than its parent 
    if smallest != i:
        A[i], A[smallest] = A[smallest], A[i] # swap
        swaps.append((i,smallest)) # Add the pairs of swap the to the swaps list
        min_heapify(A, smallest,swaps) # Heapify the root 


def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # TODO: replace by a more efficient implementation with O(n) using no 
    # more than 4𝑛 swaps to convert the array into heap.
    
    swaps=[] # initilize the swaps list
    size = int((len(data)//2)-1)
    for k in range(size, -1, -1):
        min_heapify(data,k,swaps)
    return swaps


def build_heap_naive(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps. O(n^2)
    #
    # TODO: replace by a more efficient implementation with O(n) using no 
    # more than 4𝑛 swaps to convert the array into heap.
    swaps = []
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] > data[j]:
                swaps.append((i, j))
                data[i], data[j] = data[j], data[i]
    return swaps


def testing():
    'Testing sample cases'
    # Sample1
    print("Sample1 :")
    arr1 = [5, 4, 3, 2, 1]
    print(build_heap(arr1))
    print(arr1)

    # Sample2
    print("\nSample2 :")
    arr2 = [1, 2, 3, 4, 5]
    print(build_heap(arr2))
    print(arr2)


def main():
    #####   DO NOT CHANGE THE CODE IN THIS PART #########
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
    
    """ Stress Testing """
    ### Uncomment the below comment, if you need to run the the test.
    # testing()