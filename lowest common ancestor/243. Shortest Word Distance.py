# Given an array of strings wordsDict and two different strings that already exist in the array word1 and word2, return the shortest distance between these two words in the list.


# Example 1:

# Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "coding", word2 = "practice"
# Output: 3
# Example 2:

# Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "coding"
# Output: 1


# Constraints:

# 1 <= wordsDict.length <= 3 * 104
# 1 <= wordsDict[i].length <= 10
# wordsDict[i] consists of lowercase English letters.
# word1 and word2 are in wordsDict.
# word1 != word2


class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        dic = {}
        res = float('inf')
        for i, word in enumerate(wordsDict):
            if word in dic:
                dic[word].append(i)
            else:
                dic[word] = [i]
        word1_idx = dic[word1]
        word2_idx = dic[word2]
        i, j = 0, 0
        while i < len(word1_idx) and j < len(word2_idx):
            res = min(res, abs(word1_idx[i] - word2_idx[j]))
            if word1_idx[i] < word2_idx[j]:
                i += 1
            else:
                j += 1
        return res


#one pass
class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        idx1 = idx2 = None
        res = float('inf')
        for i, word in enumerate(wordsDict):
            if word == word1:
                idx1 = i
            elif word == word2:
                idx2 = i
            if idx1 != None and idx2 != None:
                res = min(res, abs(idx1 - idx2))

        return res
