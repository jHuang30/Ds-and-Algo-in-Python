# You are given a string s, a split is called good if you can split s into 2 non-empty strings p and q where its concatenation is equal to s and the number of distinct letters in p and q are the same.

# Return the number of good splits you can make in s.

 

# Example 1:

# Input: s = "aacaba"
# Output: 2
# Explanation: There are 5 ways to split "aacaba" and 2 of them are good. 
# ("a", "acaba") Left string and right string contains 1 and 3 different letters respectively.
# ("aa", "caba") Left string and right string contains 1 and 3 different letters respectively.
# ("aac", "aba") Left string and right string contains 2 and 2 different letters respectively (good split).
# ("aaca", "ba") Left string and right string contains 2 and 2 different letters respectively (good split).
# ("aacab", "a") Left string and right string contains 3 and 1 different letters respectively.
# Example 2:

# Input: s = "abcd"
# Output: 1
# Explanation: Split the string as follows ("ab", "cd").
# Example 3:

# Input: s = "aaaaa"
# Output: 4
# Explanation: All possible splits are good.
# Example 4:

# Input: s = "acbadbaada"
# Output: 2
 

# Constraints:

# s contains only lowercase English letters.
# 1 <= s.length <= 10^5

class Solution:
    def numSplits(self, s: str) -> int:
        left, right = set(), set()
        left_list, right_list = [0] * len(s) , [0] * len(s)
        for i in range(len(s)):
            if s[i] in left:
                left_list[i] = left_list[i - 1]
            else:
                if i == 0:
                    left_list[i] = 1
                else:
                    left_list[i] = left_list[i - 1] + 1
            left.add(s[i])
        for i in range(len(s) - 1, -1, -1):
            if s[i] in right:
                right_list[i] = right_list[i + 1]
            else:
                if i == len(s) - 1:
                    right_list[i] = 1
                else:right_list[i] = right_list[i + 1] + 1
            right.add(s[i])
            
        res = 0
        for i in range(len(s) - 1):
            if left_list[i] == right_list[i + 1]:
                res += 1
        return res

class Solution:
  def numSplits(self, s: str) -> int:
      left, right, res = collections.Counter(), collections.Counter(s), 0
      for char in s:
          left[char] += 1
          right[char] -= 1
          if right[char] == 0:
              del right[char]
          if len(left) == len(right):
              res += 1
      return res