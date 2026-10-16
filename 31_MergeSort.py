def MergeSort(arr, left, right):
    if left < right:
        mid = (left + right) // 2
        MergeSort(arr, left, mid)
        MergeSort(arr, mid + 1, right)
        merge(arr, left, mid, right)

def merge(arr, left, mid, right):
    left_size = mid - left + 1
    right_size = right - mid # right - (mid + 1) + 1

    L = [0] * (left_size + 1)
    R = [0] * (right_size + 1)

    for i in range(0, left_size):
        L[i] = arr[left + i]

    L[left_size] = float('inf')  # Sentinel value

    for j in range(0, right_size):
        R[j] = arr[mid + 1 + j]

    R[right_size] = float('inf')  # Sentinel value

    i = 0
    j = 0
    # k = left

    # while i <= left_size and j <= right_size:
    for k in range(left, right + 1):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        # k += 1

    # while i < left_size:
    #     arr[k] = L[i]
    #     i += 1
    #     k += 1

    # while j < right_size:
    #     arr[k] = R[j]
    #     j += 1
    #     k += 1

arr = [12, 11, 13, 5, 6, 7]
print("Given array is:", arr)
MergeSort(arr, 0, len(arr) - 1)
print("Sorted array is:", arr)