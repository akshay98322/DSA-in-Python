def InsertionSort(arr):
    """
    Time Complexity: Best Case: O(n)
    Time Complexity: Average Case: O(n^2)
    Time Complexity: Worst Case: O(n^2)
    Auxiliary Space: O(1)
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

arr = [12, 11, 13, 5, 6]
sorted_arr = InsertionSort(arr)
print("Sorted array:", sorted_arr)