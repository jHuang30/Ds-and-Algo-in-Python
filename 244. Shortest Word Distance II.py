# Design a data structure that will be initialized with a string array, and then it should answer queries of the shortest distance between two different strings from the array.

# Implement the WordDistance class:

# WordDistance(String[] wordsDict) initializes the object with the strings array wordsDict.
# int shortest(String word1, String word2) returns the shortest distance between word1 and word2 in the array wordsDict.
 

# Example 1:

# Input
# ["WordDistance", "shortest", "shortest"]
# [[["practice", "makes", "perfect", "coding", "makes"]], ["coding", "practice"], ["makes", "coding"]]
# Output
# [null, 3, 1]

# Explanation
# WordDistance wordDistance = new WordDistance(["practice", "makes", "perfect", "coding", "makes"]);
# wordDistance.shortest("coding", "practice"); // return 3
# wordDistance.shortest("makes", "coding");    // return 1
 

# Constraints:

# 1 <= wordsDict.length <= 3 * 104
# 1 <= wordsDict[i].length <= 10
# wordsDict[i] consists of lowercase English letters.
# word1 and word2 are in wordsDict.
# word1 != word2
# At most 5000 calls will be made to shortest.


class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.words = collections.defaultdict(list)
        for idx, word in enumerate(wordsDict):
            self.words[word].append(idx)
    def shortest(self, word1: str, word2: str) -> int:
        i, j, res = 0, 0, float('inf')
        while i < len(self.words[word1]) and j < len(self.words[word2]):
            res = min(abs(self.words[word1][i] - self.words[word2][j]), res)
            if self.words[word1][i] > self.words[word2][j]:
                j += 1
            else:
                i += 1
        return res