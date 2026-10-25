def find_max_min_difference(arr):
    arr.sort()
    n = len(arr)
    mid = n // 2
    maxi = 0
    mini = 0
    j = n - 1
    for i in range(mid):
        maxi += abs(arr[j] - arr[i])
        j -= 1

        mini += abs(arr[2 * i + 1] - arr[2 * i])

    print("Maximum Difference:", maxi)
    print("Minimum Difference:", mini)

# Example usage:
arr = [12, 15, 5, 21, 20, 2, 9, 100, 9, 10]
find_max_min_difference(arr)