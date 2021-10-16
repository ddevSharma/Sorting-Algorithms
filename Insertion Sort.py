# Insertion Sort
def Insertion_sort(A, N):

    for j in range(1, N):

        key = A[j]   # First element of Unsorted Array
        i = j - 1    # Sorted Array's Last index

        while(i >= 0 and A[i] > key):

            A[i+1] = A[i]
            i -= 1

        A[i+1] = key





# Size of Array
N = int(input())
A = []

print("Enter the elements of array:")
for i in range(N):
    A.append(int(input()))

Insertion_sort(A, N)

# Displaying Sorted Array
print("Sorted Array is:-\n", A)
