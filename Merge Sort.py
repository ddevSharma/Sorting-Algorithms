# Merge Sort
def merge(A, p, q, r):

    n1 = q - p + 1
    n2 = r - (q + 1) -1  # r - q

    L = []
    R = []

    L = A[p:q+1] , float('inf')
    R = A[q + 1:r], float('inf')


    i = p
    j = q + 1

    for k in range(p, r+1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1

        else:
            A[k] = R[j]
            j += 1


def merge_sort(A, p, r):

    if p < r:
        q = (p + r) // 2
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)




# Size of Array
N = int(input())
A = []

print("Enter the elements of array:")
for i in range(N):
    A.append(int(input()))

merge_sort(A, 0, N-1)

# Displaying Sorted Array
print("Sorted Array is:-\n", A)
