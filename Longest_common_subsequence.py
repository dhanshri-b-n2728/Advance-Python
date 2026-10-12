def lcs(X, Y):
    m = len(X)
    n = len(Y)

    # Create DP table
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Reconstruct LCS
    i, j = m, n
    lcs_seq = ""

    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs_seq = X[i - 1] + lcs_seq
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return lcs_seq, dp[m][n]


# User Input
seq1 = input("Enter the first sequence: ")
seq2 = input("Enter the second sequence: ")

# Find LCS
result, length = lcs(seq1, seq2)

# Display Results
print("\nLongest Common Subsequence:", result)
print("Length of LCS:", length)