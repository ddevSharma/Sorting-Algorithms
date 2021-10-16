# Heap Sort
def PARENT(i):
    # return (i-1) // 2
    return (i//2) - 1

def LEFT(i):
    return (2 * i) + 1

def RIGHT(i):
    return (2 * i) + 2

# def Heap_Size(A):
#     return len(A)

def Max_Heapify(A, N, i):
    l = LEFT(i)
    r = RIGHT(i)

    if l < N and A[l] > A[i]:
        largest = l

    else:
        largest = i

    if r < N and A[r] > A[largest]:
        largest = r

    # Change parent node, if required
    if largest != i:
        A[largest], A[i] = A[i], A[largest]
        Max_Heapify(A, N, largest)


def Build_Max_Heap(A, N):

    N = len(A)
    # for i in range(N//2 - 1, -1, -1):
    i = PARENT(N-1)

    # i = (N-1)//2 - 1
    while i >= 0:
        Max_Heapify(A, N, i)
        i -= 1


def Heap_Sort(A, N):

    Build_Max_Heap(A,N)

    for i in range(N-1, 0, -1):

        A[0], A[i] = A[i], A[0]   # Swapping

        Max_Heapify(A, i, 0)





# Size of Array
N = int(input())
A = []

print("Enter the elements of array:")
for i in range(N):
    A.append(int(input()))

Heap_Sort(A, N)

# Displaying Sorted Array
print("Sorted Array is:-\n", A)
