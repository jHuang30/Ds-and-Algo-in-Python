# Given the root of a binary search tree, a target value, and an integer k, return the k values in the BST that are closest to the target. You may return the answer in any order.

# You are guaranteed to have only one unique set of k values in the BST that are closest to the target.


# Example 1:


# Input: root = [4, 2, 5, 1, 3], target = 3.714286, k = 2
# Output: [4, 3]
# Example 2:

# Input: root = [1], target = 0.000000, k = 1
# Output: [1]


# Constraints:

# The number of nodes in the tree is n.
# 1 <= k <= n <= 104.
# 0 <= Node.val <= 109
# -109 <= target <= 109

class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        res = []

        def dfs(root):
            if not root:
                return
            dfs(root.left)
            if len(res) == k:
                if abs(target - root.val) < abs(target - res[0]):
                    res.pop(0)
                else:
                    return
            res.append(root.val)
            dfs(root.right)

        dfs(root)
        return res
