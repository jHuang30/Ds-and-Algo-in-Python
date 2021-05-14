# Given an m x n grid of characters board and a string word, return true if word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

# Example 1:


# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true
# Example 2:


# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
# Output: true
# Example 3:


# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
# Output: false
 

# Constraints:

# m == board.length
# n = board[i].length
# 1 <= m, n <= 6
# 1 <= word.length <= 15
# board and word consists of only lowercase and uppercase English letters.

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, idx):
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[idx]:
                return False
            if idx == len(word) - 1:
                return True
            original = board[i][j]
            board[i][j] = '#'
            valid = dfs(i + 1, j, idx + 1) or dfs(i - 1, j, idx +
                                                  1) or dfs(i, j + 1, idx + 1,) or dfs(i, j - 1, idx + 1)
            board[i][j] = original
            return valid

        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
        return False
