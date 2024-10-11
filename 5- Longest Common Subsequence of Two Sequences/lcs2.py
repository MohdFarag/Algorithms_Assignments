#Uses python3
import sys
import random

# An Enhanced Algorithm
def lcs2(a, b) :
    n = len(a)
    m = len(b)
    
    # make matrix of zeros with size n+1 * m+1
    L = [[0 for x in range(m+1)] for x in range(n+1)]
 
    for i in range(n+1):
        for j in range(m+1):
            if i == 0 or j == 0 :
            # Fill the first row and columns with zeros (Initial Values)
                L[i][j] = 0
            elif a[i-1] == b[j-1]:
            # If matching
                L[i][j] = L[i-1][j-1]+1
            else:
            # If not matching
                L[i][j] = max(L[i-1][j] , L[i][j-1])

    return L[n][m] # Return the last element in the matrix

# A Naive recursive 
def lcs(X, Y, m, n):
    if m == 0 or n == 0:
        return 0
    elif X[m-1] == Y[n-1]:
        return 1 + lcs(X, Y, m-1, n-1)
    else:
        return max(lcs(X, Y, m, n-1), lcs(X, Y, m-1, n))


def Stress_Testing():
    '''Stress Testing'''
    # First Check
    a = [2, 3, 4, 5, 6]
    b = [3, 4, 2, 4, 5]

    print(lcs(a, b,len(a), len(b)))
    print(lcs2(a, b))
    
    _ = input("Start the stress Testing... Press Enter!")

    while True :
        n,m = random.randint(1,10),random.randint(1,10)
        a = [random.randint(-10,10) for _ in range(0,n)]
        b = [random.randint(-10,10) for _ in range(0,m)]
        print(a,n)
        print(b,m)

        if lcs2(a, b) == lcs(a, b, n, m) :
            print(True)
            print(lcs2(a, b))
        else :
            break    


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
        
    """Stress Testing"""
    ### Uncomment the below comment, if you need to run the the test.
    #Stress_Testing()