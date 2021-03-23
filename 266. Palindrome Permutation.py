# Given a string s, return true if a permutation of the string could form a palindrome.

 

# Example 1:

# Input: s = "code"
# Output: false
# Example 2:

# Input: s = "aab"
# Output: true
# Example 3:

# Input: s = "carerac"
# Output: true
 

# Constraints:

# 1 <= s.length <= 5000
# s consists of only lowercase English letters.

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        counter = collections.Counter(s)
        res = 0
        for count in counter.values():
            if count % 2:
                res += 1
            if res > 1:
                return False
        return True