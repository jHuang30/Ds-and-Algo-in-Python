# Given a string s, return the longest palindromic substring in s.


# Example 1:

# Input: s = "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"
# Example 3:

# Input: s = "a"
# Output: "a"
# Example 4:

# Input: s = "ac"
# Output: "a"


# Constraints:

# 1 <= s.length <= 1000
# s consist of only digits and English letters(lower-case and / or upper-case),

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        self.start = 0
        self.max_len = 0

        def find_len(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            if right - left - 1 > self.max_len:
                self.max_len = right - left - 1
                self.start = left + 1

        for i in range(len(s)):
            find_len(i, i)
            find_len(i, i + 1)
        return s[self.start:self.start + self.max_len]
