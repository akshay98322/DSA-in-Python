# 0-1 knapsack problem recursive

def knapsack_recursive(weights, values, capacity, n):
    # Base case: no items left or capacity is 0
    if n == 0 or capacity == 0:
        return 0

    # If weight of the nth item is more than the capacity, skip it
    if weights[n - 1] > capacity:
        return knapsack_recursive(weights, values, capacity, n - 1)

    # Return the maximum of including the nth item or not including it
    else:
        include_item = values[n - 1] + knapsack_recursive(weights, values, capacity - weights[n - 1], n - 1)
        exclude_item = knapsack_recursive(weights, values, capacity, n - 1)
        return max(include_item, exclude_item)

# Example usage
if __name__ == "__main__":
    weights = [2,3,4,5]
    values = [3,4,5,6]
    capacity = 5
    n = len(values)
    max_value = knapsack_recursive(weights, values, capacity, n)
    print(f"Maximum value in knapsack: {max_value}")