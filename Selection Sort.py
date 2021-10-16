# Selection Sort
def Selection_Sort(A, N):
    for i in range(N):
        min = i  # Considering 1st element of unsorted array as min. element

        # As after i iterations first i elements will already be in place
        for j in range(i + 1, N):
            if A[min] > A[j]:
                min = j

        A[i], A[min] = A[min], A[i]


# Size of Array
N = int(input())
A = []

print("Enter the elements of array:")
for i in range(N):
    A.append(int(input()))

Selection_Sort(A, N)

# Displaying Sorted Array
print("Sorted Array is:-\n", A)
