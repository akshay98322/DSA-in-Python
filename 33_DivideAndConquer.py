# find the max and min of an array using divide and conquer
def find_max_min(arr, low, high):
    """
    Time Complexity: Best Case: O(n)
    Time Complexity: Average Case: O(n)
    Time Complexity: Worst Case: O(n)
    Auxiliary Space: O(log n)
    """
    # single element
    if low == high:
        return arr[low], arr[high]
    # two elements
    elif high == low + 1:
        if arr[low] > arr[high]:
            return arr[low], arr[high]
        else:
            return arr[high], arr[low]
    # more than two elements
    else:
        mid = (low + high) // 2
        max1, min1 = find_max_min(arr, low, mid)
        max2, min2 = find_max_min(arr, mid + 1, high)
        return max(max1, max2), min(min1, min2)

# Example usage
arr = [3, 5, 1, 8, 2, 7, 4, 6]
max_value, min_value = find_max_min(arr, 0, len(arr) - 1)
print("Original array:", arr)
print("Maximum value:", max_value)
print("Minimum value:", min_value)