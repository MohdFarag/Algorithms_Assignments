"""Matrix multiplication Code"""

# Uses python3
import random
import numpy as np

# To fill matrix with zeros up to lowest power two
## Using NumPy - Faster than Bottom
def add_zeros_matrix_power_two(A, B):
    n = len(A)
    while not (n and (not (n & (n - 1)))):
        n += 1
        A = np.hstack((A, np.zeros((A.shape[0], 1))))
        A = np.vstack((A, np.zeros((1, A.shape[1]))))

        B = np.hstack((B, np.zeros((B.shape[0], 1))))
        B = np.vstack((B, np.zeros((1, B.shape[1]))))

    return (A, B)

# Without NumPy - Complexity = O(n^3) !!
# def add_zeros_matrix_power_two(A,B):
#     # Add columns and rows to the nearest power 2 number
#     n = len(A)
#     if not(n and (not (n & (n - 1)))):
#         while not(n and (not (n & (n - 1)))):
#             n += 1
#             A1 = np.zeros((n, n))
#             B1 = np.zeros((n, n))
#
#             for i in range(len(A)):
#                 for j in range(len(A)):
#                     A1[i, j] = A[i, j]
#                     B1[i, j] = B[i, j]
#     else:
#         return (A,B)
#
#     return (A1,B1)


# Divide & Conquer
## Divide & Conquer (Strassen’s)
def matrix_mult_fast(A, B, sizeN):

    # Add columns and rows to the nearest power 2 number for A and B
    A, B = add_zeros_matrix_power_two(A, B)

    n = len(A)
    product = np.zeros((n, n))

    if n == 1:
        return A * B
    else:  # Recursion Case
        N = int(n / 2)

        # Divide matrix A for 4 matrices, each matrix has dimension = (n/2 * n/2)
        a11 = A[:N, :N]
        a12 = A[:N, N:]
        a21 = A[N:, :N]
        a22 = A[N:, N:]

        # Divide matrix B for 4 matrices, each matrix has dimension = (n/2 * n/2)
        b11 = B[:N, :N]
        b12 = B[:N, N:]
        b21 = B[N:, :N]
        b22 = B[N:, N:]

        # Computing the 7 products
        m1 = matrix_mult_fast(a11+a22, b11+b22, N)
        m2 = matrix_mult_fast(a21+a22, b11, N)
        m3 = matrix_mult_fast(a11, b12-b22, N)
        m4 = matrix_mult_fast(a22, b21-b11, N)
        m5 = matrix_mult_fast(a11 + a12, b22, N)
        m6 = matrix_mult_fast(a21-a11, b11+b12, N)
        m7 = matrix_mult_fast(a12-a22, b21+b22, N)

        # Computing the values of the 4 quadrants of the final matrix
        product[:N, :N] = m1 + m4 - m5 + m7
        product[:N, N:] = m3 + m5
        product[N:, :N] = m2 + m4
        product[N:, N:] = m1 - m2 + m3 + m6

    return product[:sizeN, :sizeN]

# Naive Divide & conquer
def matrix_mult(A, B, sizeN):

    # Add columns and rows to the nearest power 2 number for A and B
    A, B = add_zeros_matrix_power_two(A, B)

    n = len(A)
    C = np.zeros((n, n))

    if n == 1:  # Base case
        return A * B  # Multiply one by one
    else:  # Recursion Case

        N = int(n / 2)  # Split size of matrix to half

        # Divide matrix A for 4 matrices, each matrix has dimension = (n/2 * n/2)
        a11 = A[:N, :N]
        a12 = A[:N, N:]
        a21 = A[N:, :N]
        a22 = A[N:, N:]

        # Divide matrix B for 4 matrices, each matrix has dimension = (n/2 * n/2)
        b11 = B[:N, :N]
        b12 = B[:N, N:]
        b21 = B[N:, :N]
        b22 = B[N:, N:]

        # Divide the problems to the smaller problems, then Conquer it in C
        C[:N, :N] = matrix_mult(a11, b11, N) + matrix_mult(a12, b21, N)
        C[:N, N:] = matrix_mult(a11, b12, N) + matrix_mult(a12, b22, N)
        C[N:, :N] = matrix_mult(a21, b11, N) + matrix_mult(a22, b21, N)
        C[N:, N:] = matrix_mult(a21, b12, N) + matrix_mult(a22, b22, N)

    # Return C from 1 to sizeN (The default size) to eliminate zeros that resulted
    # from (add_zeros_matrix_power_two) function
    return C[:sizeN, :sizeN]


# Without Divide & Conquer
## Naive
def matrix_mult_naive(A, B, n):
    product = np.zeros((n, n))

    for i in range(n):
        for j in range(n):
            for k in range(n):
                product[i, j] += A[i, k] * B[k, j]

    return product

# Enhanced than naive
def matrix_mult_fast_noDC(A, B, n):
    product = np.zeros((n, n))

    for i in range(len(A)):
        for j in range(len(B)):
            product[:, i] += A[:, j] * B[j, i]

    return product


def stress_testing(mode):
    # --- Stress Testing --- #
    """Stress Testing"""

    while True:
        n = random.randint(1, 20)
        A = []
        B = []

        for _ in range(n):
            A.append([random.randint(-2 ** 10, 2 ** 10) for j in range(n)])

        for _ in range(n):
            B.append([random.randint(-2 ** 10, 2 ** 10) for j in range(n)])

        A = np.array(A)
        B = np.array(B)

        print("n =", n)
        print("A=", A)
        print("B=", B)
        print("-" * 10)

        if mode == 1 :
            """Multiply without D&C (naive)"""
            if np.array_equal(np.matmul(A, B), matrix_mult_naive(A, B, n)):
                print(True)
            else:
                print("true=", np.matmul(A, B))
                print("wrong=", matrix_mult_naive(A, B, n))
                print(False)
                break

        elif mode == 2 :
            """Multiply without D&C (fast)"""
            if np.array_equal(np.matmul(A, B), matrix_mult_fast_noDC(A, B, n)):
                print(True)
            else:
                print("true=", np.matmul(A, B))
                print("wrong=", matrix_mult_fast_noDC(A, B, n))
                print(False)
                break

        elif mode == 3 :
            """Multiply with D&C"""
            if np.array_equal(np.matmul(A, B), matrix_mult(A, B, n)):
                print(True)
            else:
                print("true=", np.matmul(A, B))
                print("wrong=", matrix_mult(A, B, n))
                print(False)
                break

        elif mode == 4 :
            """Multiply with D&C Enhanced"""
            if np.array_equal(np.matmul(A, B), matrix_mult_fast(A, B, n)):
                print(True)
            else:
                print(False)
                break

if __name__ == "__main__":
    AGAIN = "1"
    while AGAIN == "1" :
        n = int(input())
        A = []
        B = []

        # Enter matrix 1 values, press enter after each row
        # Matrix 1 filling
        for i in range(n):
            A.append([int(j) for j in input().split()])

        # Enter matrix 2 values, press enter after each row
        # Matrix 2 filling
        for i in range(n):
            B.append([int(j) for j in input().split()])

        A = np.array(A)
        B = np.array(B)

        # print(matrix_mult(A, B, n))
        print(matrix_mult_fast(A, B, n))

        AGAIN = input("""Enter:
                    1 if you want to make another multiplication.
                    2 if you want to make stress testing on the code, other if exit.
                    """)

    if AGAIN == "2" :
        PARAGRAPH = """
        1- Multiply without D&C Naive
        2- Multiply without D&C Enhanced
        3- Multiply with D&C Naive
        4- Multiply with D&C Enhanced
        """
        print(PARAGRAPH)

        n = input("Enter number of testing you want to make:")
        stress_testing(int(n))
