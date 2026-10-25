# Top-Down Approach (Memoization)
def knapsack_top_down(weights, values, capacity, n, memo):
    if n == 0 or capacity == 0:
        return 0

    if memo[n][capacity] != -1:
        return memo[n][capacity]

    if weights[n - 1] > capacity:
        memo[n][capacity] = knapsack_top_down(
            weights, values, capacity, n - 1, memo
        )
    else:
        include = values[n - 1] + knapsack_top_down(
            weights, values, capacity - weights[n - 1], n - 1, memo
        )
        exclude = knapsack_top_down(
            weights, values, capacity, n - 1, memo
        )
        memo[n][capacity] = max(include, exclude)

    return memo[n][capacity]


# Bottom-Up Approach
def knapsack_bottom_up(weights, values, capacity):
    n = len(weights)

    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


# User Input Section
n = int(input("Enter number of items: "))

weights = []
values = []

for i in range(n):
    weight = int(input(f"Enter weight of item {i + 1}: "))
    value = int(input(f"Enter value of item {i + 1}: "))

    weights.append(weight)
    values.append(value)

capacity = int(input("Enter knapsack capacity: "))

# Top-Down Execution
memo = [[-1 for _ in range(capacity + 1)] for _ in range(n + 1)]
top_down_result = knapsack_top_down(
    weights, values, capacity, n, memo
)

# Bottom-Up Execution
bottom_up_result = knapsack_bottom_up(
    weights, values, capacity
)

# Display Results
print("\n--- Results ---")
print("Maximum Value (Top-Down):", top_down_result)
print("Maximum Value (Bottom-Up):", bottom_up_result)