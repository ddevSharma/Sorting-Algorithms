# Bucket Sort

# Insertion Sort
def Insertion_sort(A):

    for j in range(1, len(A)):

        key = A[j]   # First element of Unsorted Array
        i = j - 1    # Sorted Array's Last index

        while(i >= 0 and A[i] > key):

            A[i+1] = A[i]
            i -= 1

        A[i+1] = key

    return A

# Bucket Sort
def Bucket_Sort(A, N):

    B = []
    Slots = 10  # 10 slots, each of size 0.1

    for i in range(Slots):
        B.append([])

    # Putting Array Elements in Buckets
    for i in range(N):
        index = int(Slots * A[i])
        B[index].append(A[i])

    # Sorting each bucket using Insertion Sort
    for i in range(Slots):
        B[i] = Insertion_sort(B[i])

    # Concatenating the Resulting Buckets
    k = 0
    for i in range(Slots):
        for j in range(len(B[i])):
            A[k] = B[i][j]
            k += 1






# Size of Array
N = int(input())
A = []

print("Enter the elements of array:")
for i in range(N):
    A.append(float(input()))

Bucket_Sort(A, N)

# Displaying Sorted Array
print("Sorted Array is:-\n", A)
