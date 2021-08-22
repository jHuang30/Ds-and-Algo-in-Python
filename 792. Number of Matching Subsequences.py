# Given a string s and an array of strings words, return the number of words[i] that is a subsequence of s.

# A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

# For example, "ace" is a subsequence of "abcde".
 

# Example 1:

# Input: s = "abcde", words = ["a","bb","acd","ace"]
# Output: 3
# Explanation: There are three strings in words that are a subsequence of s: "a", "acd", "ace".
# Example 2:

# Input: s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
# Output: 2
 

# Constraints:

# 1 <= s.length <= 5 * 104
# 1 <= words.length <= 5000
# 1 <= words[i].length <= 50
# s and words[i] consist of only lowercase English letters.

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        dic = defaultdict(list)
        res = 0
        for word in words:
            dic[word[0]].append(word)
        for char in s:
            candidates = dic[char]
            dic[char] = []
            for word in candidates:
                if len(word) == 1:
                    res += 1
                else:
                    dic[word[1]].append(word[1:])
        return res