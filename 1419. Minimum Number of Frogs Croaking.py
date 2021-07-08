# Given the string croakOfFrogs, which represents a combination of the string "croak" from different frogs, that is, multiple frogs can croak at the same time, so multiple “croak” are mixed. Return the minimum number of different frogs to finish all the croak in the given string.

# A valid "croak" means a frog is printing 5 letters ‘c’, ’r’, ’o’, ’a’, ’k’ sequentially. The frogs have to print all five letters to finish a croak. If the given string is not a combination of valid "croak" return -1.

 

# Example 1:

# Input: croakOfFrogs = "croakcroak"
# Output: 1 
# Explanation: One frog yelling "croak" twice.
# Example 2:

# Input: croakOfFrogs = "crcoakroak"
# Output: 2 
# Explanation: The minimum number of frogs is two. 
# The first frog could yell "crcoakroak".
# The second frog could yell later "crcoakroak".
# Example 3:

# Input: croakOfFrogs = "croakcrook"
# Output: -1
# Explanation: The given string is an invalid combination of "croak" from different frogs.
# Example 4:

# Input: croakOfFrogs = "croakcroa"
# Output: -1
 

# Constraints:

# 1 <= croakOfFrogs.length <= 10^5
# All characters in the string are: 'c', 'r', 'o', 'a' or 'k'.

class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        if len(croakOfFrogs) % 5:
            return -1
        letter_freq = {'c': 0, 'r': 0, 'o': 0, 'a': 0, 'k': 0}
        current_num = 0
        res = 0
        for char in croakOfFrogs:
            if char == 'c':
                current_num += 1
                res = max(res, current_num)
            if char == 'r':
                if letter_freq[char] == letter_freq['c']:
                    return -1
            if char == 'o':
                if letter_freq[char] == letter_freq['r']:
                    return -1
            if char == 'a':
                if letter_freq[char] == letter_freq['o']:
                    return -1
            if char == 'k':
                if letter_freq[char] == letter_freq['a']:
                    return -1
                current_num -= 1
            letter_freq[char] += 1

        return res if current_num == 0 else -1


# using index and arr:

class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        if len(croakOfFrogs) % 5:
            return -1
        letter_freq = [0] * 5
        current_num = 0
        res = 0
        for char in croakOfFrogs:
            idx = 'croak'.index(char)
            if idx == 0:
                current_num += 1
                res = max(res, current_num)
            elif letter_freq[idx] == letter_freq[idx - 1]:
                return -1
            elif idx == 4:
                current_num -= 1
            letter_freq[idx] += 1

        return res if current_num == 0 else -1
