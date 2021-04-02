# Numbers can be regarded as the product of their factors.

# For example, 8 = 2 x 2 x 2 = 2 x 4.
# Given an integer n, return all possible combinations of its factors. You may return the answer in any order.

# Note that the factors should be in the range[2, n - 1].


# Example 1:

# Input: n = 1
# Output: []
# Example 2:

# Input: n = 12
# Output: [[2, 6], [3, 4], [2, 2, 3]]
# Example 3:

# Input: n = 37
# Output: []
# Example 4:

# Input: n = 32
# Output: [[2, 16], [4, 8], [2, 2, 8], [2, 4, 4], [2, 2, 2, 4], [2, 2, 2, 2, 2]]


# Constraints:

# 1 <= n <= 108


class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        res = []

        def dfs(n, start, temp):
            for i in range(start, int(sqrt(n)) + 1):
                if n % i == 0:
                    temp.append(i)
                    temp.append(n // i)
                    res.append(temp.copy())
                    temp.pop()
                    dfs(n // i, i, temp)
                    temp.pop()

        dfs(n, 2, [])
        return res
