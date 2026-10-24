def BubbleSort(arr):
    """
    Time Complexity: Best Case: O(n^2) 
    Time Complexity: Average Case: O(n^2)
    Time Complexity: Worst Case: O(n^2)
    Auxiliary Space: O(1)
    """
    n = len(arr)
    for i in range(n):
        # Last i elements are already sorted
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
print("Original array:", arr)
sorted_arr = BubbleSort(arr)
print("Sorted array:", sorted_arr)