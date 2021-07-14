# Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.


# Example 1:

# Input: s = "abab"
# Output: true
# Explanation: It is the substring "ab" twice.
# Example 2:

# Input: s = "aba"
# Output: false
# Example 3:

# Input: s = "abcabcabcabc"
# Output: true
# Explanation: It is the substring "abc" four times or the substring "abcabc" twice.


# Constraints:

# 1 <= s.length <= 104
# s consists of lowercase English letters.

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(len(s) - 1):  # can also be range(0, len(s) // 2):
            current = s[0:i + 1]
            if len(s) % len(current) == 0:
                if current * (len(s) // len(current)) == s:
                    return True
        return False



# 2
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        new_str = (s * 2)[1:-1]
        return new_str.find(s) != -1
