# 0-1 knapsack problem using dynamic programming using memoization

def knapsack_dp(weights, values, capacity):
    n = len(values)
    # Create a memoization table to store the maximum value at each n and capacity
    memo = [[-1 for _ in range(capacity + 1)] for _ in range(n + 1)]

    def knapsack_helper(i, w):
        # Base case: no items left or capacity is 0
        if i == 0 or w == 0:
            return 0

        # If the value is already computed, return it
        if memo[i][w] != -1:
            return memo[i][w]

        # If weight of the ith item is more than the capacity, skip it
        if weights[i - 1] > w:
            memo[i][w] = knapsack_helper(i - 1, w)
        else:
            # Return the maximum of including the ith item or not including it
            include_item = values[i - 1] + knapsack_helper(i - 1, w - weights[i - 1])
            exclude_item = knapsack_helper(i - 1, w)
            memo[i][w] = max(include_item, exclude_item)

        return memo[i][w]

    return knapsack_helper(n, capacity)

# Example usage
if __name__ == "__main__":
    weights = [2, 3, 4, 5]
    values = [3, 4, 5, 6]
    capacity = 6
    max_value = knapsack_dp(weights, values, capacity)
    print(f"Maximum value in knapsack: {max_value}")