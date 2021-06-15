# Given a binary tree, return the sum of values of nodes with even-valued grandparent.  (A grandparent of a node is the parent of its parent, if it exists.)

# If there are no nodes with an even-valued grandparent, return 0.


# Example 1:


# Input: root = [6, 7, 8, 2, 7, 1, 3, 9, null, 1, 4, null, null, null, 5]
# Output: 18
# Explanation: The red nodes are the nodes with even-value grandparent while the blue nodes are the even-value grandparents.


# Constraints:

# The number of nodes in the tree is between 1 and 10 ^ 4.
# The value of nodes is between 1 and 100.

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        res = 0
        queue = [[root, False, False]]
        while queue:
            [current, parent_even, grand_even] = queue.pop(0)
            if grand_even:
                res += current.val
            if current.left:
                queue.append([current.left, current.val % 2 == 0, parent_even])
            if current.right:
                queue.append([current.right, current.val %
                             2 == 0, parent_even])

        return res


# dfs:

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.res = 0

        def dfs(root, parent, grandParent):
            if not root:
                return
            if grandParent:
                self.res += root.val
            dfs(root.left, root.val % 2 == 0, parent)
            dfs(root.right, root.val % 2 == 0, parent)

        dfs(root, False, False)
        return self.res
