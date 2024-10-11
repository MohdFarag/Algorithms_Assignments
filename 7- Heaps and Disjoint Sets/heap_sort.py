#python3
import sys
import random

## HeapSort sorts in place ##


# return left child
def leftChild(i):
    return 2 * i + 1

# return right child
def rightChild(i):
    return 2 * i + 2

def heapify(arr, n, i):
    left = leftChild(i) # return left child of givin index
    right = rightChild(i) # return right child of givin index

    ### Find the index of largest value between given index, left and right

    if left < n and arr[left] > arr[i]: # largest = index of max(A[left],A[i])
        largest = left
    else:
        largest = i
    
    if right < n and arr[right] > arr[largest]: # largest = index of max(A[right],A[largest])
        largest = right

    # If there is a child more than its parent
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i] # swap
        heapify(arr, n, largest) # Heapify the root

def heap_sort(arr):
    # Write your code here
    n = len(arr)
    
    # Build max heap
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n ,i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap
        heapify(arr, i, 0) # Heapify root element


def stress_testing():
    # Sample 1
    arr = [5, 4, 3, 2, 1]
    heap_sort(arr)
    print(arr)

    # Sample 2
    arr = [12, 11, 13, 5, 6, 7]
    heap_sort(arr)
    print(arr)

    _ = input("Start the stress Testing... Press Enter!")

    while True :
        n = random.randint(10,20)
        arr1 = [random.randint(0,100) for _ in range(0,n)]
        arr2 = arr1.copy()
        
        heap_sort(arr1)
        arr2.sort()

        if arr1 == arr2 :
            print(True)
        else :
            print("ERROR !!")
            break   

### DO NOT CHANGE INPUT/OUTPUT FORMAT ####

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    heap_sort(a)
    for x in a:
        print(x, end=' ')

    "Testing"
    ### Uncomment the below comment, if you need to run the the test.
    # stress_testing()