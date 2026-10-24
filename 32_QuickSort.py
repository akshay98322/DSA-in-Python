def QuickSort(arr, l, r):
    """
    Considering the first element as pivot, the time complexity of QuickSort is:
    Time Complexity: Best Case: O(n log n)
    Time Complexity: Average Case: O(n log n)
    Time Complexity: Worst Case: O(n^2)
    Auxiliary Space: O(log n)
    """
    if l < r:
        pi = partition(arr, l, r)
        QuickSort(arr, l, pi - 1)
        QuickSort(arr, pi + 1, r)

def partition(arr, l, r):
    pivot = arr[l]
    i = l + 1
    j = r
    while True:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break
    arr[l], arr[j] = arr[j], arr[l]
    return j


# Example usage
arr = [22, 64, 34, 22, 25, 12, 22, 11]
print("Original array:", arr)
QuickSort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)