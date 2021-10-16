# Counting Sort
def Counting_Sort(A, N):

    B = [0 for i in range(N)]
    C = [0 for i in range(N)]

    for j in range(1, N):

        C[A[j]] += 1

    for i in range(1, N):
        C[i] = C[i] + C[i - 1]

    for j in range(N-1, 0, -1):
        B[C[A[j]]] = A[j]
        C[A[j]] = C[A[j]] - 1

    return B





# Size of Array
N = int(input())
A = []

print("Enter the elements of array:")
for i in range(N):
    A.append(int(input()))

# Displaying Sorted Array
print("Sorted Array is:-")
print(Counting_Sort(A, N))

