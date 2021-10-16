# Quick Sort
def Partition(A, p, r):

    # Pivot Element
    x = A[r]

    i = p - 1

    for j in range(p, r):
        if A[j] <= x:
            i += 1

            A[i], A[j] = A[j], A[i]

    A[i + 1], A[r] = A[r], A[i + 1]

    return i + 1



def quick_sort(A, p, r):

    if p < r:
        q = Partition(A, p, r)
        quick_sort(A, p, q-1)
        quick_sort(A, q + 1, r)




# Size of Array
N = int(input())
A = []

print("Enter the elements of array:")
for i in range(N):
    A.append(int(input()))

quick_sort(A, 0, N-1)

# Displaying Sorted Array
print("Sorted Array is:-\n", A)
