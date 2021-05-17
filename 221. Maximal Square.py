# Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.


# Example 1:


# Input: matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], [
#     "1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]
# Output: 4
# Example 2:


# Input: matrix = [["0", "1"], ["1", "0"]]
# Output: 1
# Example 3:

# Input: matrix = [["0"]]
# Output: 0


# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 300
# matrix[i][j] is '0' or '1'.

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = [0] * len(matrix[0])
        max_len = 0
        prev = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                temp = dp[j]
                if i == 0 or j == 0:
                    dp[j] = int(matrix[i][j])
                elif matrix[i][j] == '1':
                    dp[j] = min(dp[j], dp[j - 1], prev) + 1
                else:
                    dp[j] = 0
                max_len = max(max_len, dp[j])
                prev = temp
        return max_len * max_len
