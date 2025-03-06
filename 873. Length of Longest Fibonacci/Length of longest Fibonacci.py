class Solution:
    def lenLongestFibSubseq(self, arr):  # Had to remove type Hints 
        n = len(arr)
        if n < 3:
            return 0  # Fibonacci sequence must have at least 3 numbers

        max_len = 0
        dp = [[2] * n for _ in range(n)]  # Initialize DP with 2 instead of 0
        val_to_idx = {num: idx for idx, num in enumerate(arr)}

        for curr in range(n):
            for prev in range(curr):
                diff = arr[curr] - arr[prev]
                prev_idx = val_to_idx.get(diff, -1)

                if prev_idx >= 0 and prev_idx < prev:  # Ensure valid sequence
                    dp[prev][curr] = dp[prev_idx][prev] + 1
                    max_len = max(max_len, dp[prev][curr])

        return max_len if max_len > 2 else 0

# Test arrays
# arr = [1,2,3,4,5,6,7,8]

# arr = [1,3,7,11,12,14,18]

