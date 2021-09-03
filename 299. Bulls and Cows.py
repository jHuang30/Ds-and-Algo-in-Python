# You are playing the Bulls and Cows game with your friend.

# You write down a secret number and ask your friend to guess what the number is . When your friend makes a guess, you provide a hint with the following info:

# The number of "bulls", which are digits in the guess that are in the correct position.
# The number of "cows", which are digits in the guess that are in your secret number but are located in the wrong position. Specifically, the non-bull digits in the guess that could be rearranged such that they become bulls.
# Given the secret number secret and your friend's guess guess, return the hint for your friend's guess.

# The hint should be formatted as "xAyB", where x is the number of bulls and y is the number of cows. Note that both secret and guess may contain duplicate digits.


# Example 1:

# Input: secret = "1807", guess = "7810"
# Output: "1A3B"
# Explanation: Bulls are connected with a '|' and cows are underlined:
# "1807"
# |
# "7810"
# Example 2:

# Input: secret = "1123", guess = "0111"
# Output: "1A1B"
# Explanation: Bulls are connected with a '|' and cows are underlined:
# "1123"        "1123"
# | or |
# "0111"        "0111"
# Note that only one of the two unmatched 1s is counted as a cow since the non-bull digits can only be rearranged to allow one 1 to be a bull.
# Example 3:

# Input: secret = "1", guess = "0"
# Output: "0A0B"
# Example 4:

# Input: secret = "1", guess = "1"
# Output: "1A0B"


# Constraints:

# 1 <= secret.length, guess.length <= 1000
# secret.length == guess.length
# secret and guess consist of digits only.


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        cows = bulls = 0
        guessHsh = {}
        secretHsh = {}
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                guessHsh[guess[i]] = guessHsh.get(guess[i], 0) + 1
                secretHsh[secret[i]] = secretHsh.get(secret[i], 0) + 1

        for num in guessHsh:
            if num in secretHsh:
                cows += min(guessHsh[num], secretHsh[num])

        return str(bulls) + 'A' + str(cows) + 'B'


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        dic = collections.Counter(secret)
        common_letters = 0
        for num in guess:
            if dic[num] > 0:
                common_letters += 1
                dic[num] -= 1
        a_num = 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                a_num += 1
        b_num = common_letters - a_num
        
        return str(a_num) + 'A' + str(b_num) + 'B'