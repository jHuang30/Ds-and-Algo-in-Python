# An attendance record for a student can be represented as a string where each character signifies whether the student was absent, late, or present on that day. The record only contains the following three characters:

# 'A': Absent.
# 'L': Late.
# 'P': Present.
# Any student is eligible for an attendance award if they meet both of the following criteria:

# The student was absent ('A') for strictly fewer than 2 days total.
# The student was never late ('L') for 3 or more consecutive days.
# Given an integer n, return the number of possible attendance records of length n that make a student eligible for an attendance award. The answer may be very large, so return it modulo 109 + 7.

 

# Example 1:

# Input: n = 2
# Output: 8
# Explanation: There are 8 records with length 2 that are eligible for an award:
# "PP", "AP", "PA", "LP", "PL", "AL", "LA", "LL"
# Only "AA" is not eligible because there are 2 absences (there need to be fewer than 2).
# Example 2:

# Input: n = 1
# Output: 3
# Example 3:

# Input: n = 10101
# Output: 183236316
 

# Constraints:

# 1 <= n <= 105

#2^n LTE
class Solution:
    def checkRecord(self, n: int) -> int:
        def dfs(n, total_absent, total_late):
            if n == 0:
                return 1
            res = 0
            if total_late < 2:
                res += dfs(n - 1, total_absent, total_late + 1)
            if total_absent < 1:
                res += dfs(n - 1, total_absent + 1, total_late)
            res += dfs(n - 1, total_absent, 0)
            return res
        return dfs(n, 0, 0)

#n LTE memoization

class Solution:
    def checkRecord(self, n: int) -> int:
        memo = {}
        def dfs(n, total_absent, total_late):
            if n == 0:
                return 1
            if f"{n}-{total_absent}-{total_late}" in memo:
                return memo[f"{n}-{total_absent}-{total_late}"]
            res = 0
            if total_late < 2:
                res += dfs(n - 1, total_absent, total_late + 1)
            if total_absent < 1:
                res += dfs(n - 1, total_absent + 1, 0)
            res += dfs(n - 1, total_absent, 0)
            memo[f"{n}-{total_absent}-{total_late}"] = res % (10 ** 9 + 7)
            return res % (10 ** 9 + 7)
        return dfs(n, 0, 0)