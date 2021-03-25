# Given a string s and an integer k, return the length of the longest substring of s that contains at most k distinct characters.

 

# Example 1:

# Input: s = "eceba", k = 2
# Output: 3
# Explanation: The substring is "ece" with length 3.
# Example 2:

# Input: s = "aa", k = 1
# Output: 2
# Explanation: The substring is "aa" with length 2.
 

# Constraints:

# 1 <= s.length <= 5 * 104
# 0 <= k <= 50

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        char_with_idx = collections.defaultdict(int)
        start, res = 0, 0
        for end in range(len(s)):
            char_with_idx[s[end]] += 1
            while len(char_with_idx) > k:
                char_with_idx[s[start]] -= 1
                if char_with_idx[s[start]] == 0:
                    del char_with_idx[s[start]]
                start += 1
            res = max(res, end - start + 1)
        return res