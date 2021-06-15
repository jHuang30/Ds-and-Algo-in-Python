# Given the root of a binary tree, return the sum of values of its deepest leaves.


# Example 1:


# Input: root = [1, 2, 3, 4, 5, null, 6, 7, null, null, null, null, 8]
# Output: 15
# Example 2:

# Input: root = [6, 7, 8, 2, 7, 1, 3, 9, null, 1, 4, null, null, null, 5]
# Output: 19

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        res = 0
        queue = [root]
        while queue:
            res = 0
            size = len(queue)
            for i in range(size):
                current = queue.pop(0)
                res += current.val
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
        return res
