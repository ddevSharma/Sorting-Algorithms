# Bubble Sort
def Bubble_sort(A, N):
    for i in range(N):

        # As after i iterations last i elements will already be in place
        for j in range(N - i - 1):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]


# Size of Array
N = int(input())
A = []

print("Enter the elements of array:")
for i in range(N):
    A.append(int(input()))

Bubble_sort(A, N)

# Displaying Sorted Array
print("Sorted Array is:-\n", A)
