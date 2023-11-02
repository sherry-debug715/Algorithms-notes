def highest_reachable_index(steps, bad_element):
    # Initialize the dynamic programming table where dp[i][j] represents
    # the highest index that can be reached at step i with a jump size of j.
    # We need steps+2 rows because we start counting steps from 1, and we need anadditional row for step 0. We need steps+2 columns for the same reason.
    dp = [[-1 for _ in range(steps + 2)] for _ in range(steps + 2)]
    
    # Base case initialization, at step 0 we are at index 0 and jump size is 1
    dp[0][1] = 0
    
    # Fill the dp table
    for i in range(1, steps + 1):  # For each step
        for j in range(1, i + 2):  # For each jump size
            # We can either stay at the current index or jump from the index we were at in the previous step
            stay = dp[i - 1][j]
            jump = dp[i - 1][j - 1] + j if dp[i - 1][j - 1] != -1 else -1
            
            # Choose the action that gives us the highest index, avoiding the bad element
            dp[i][j] = max(stay, jump) if jump != bad_element else stay

    # The result is the maximum index reached at the last step, ignoring the jump size
    # as we want the highest index regardless of the jump size.
    return max(dp[steps])

# Example usage:
highest_reachable_index(4, 3)  # Should return 6, since the jumps can be 1-2-3 (and skip 3)
