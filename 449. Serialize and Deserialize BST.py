# Serialization is converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

# Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You need to ensure that a binary search tree can be serialized to a string, and this string can be deserialized to the original tree structure.

# The encoded string should be as compact as possible.


# Example 1:

# Input: root = [2, 1, 3]
# Output: [2, 1, 3]
# Example 2:

# Input: root = []
# Output: []


# Constraints:

# The number of nodes in the tree is in the range[0, 104].
# 0 <= Node.val <= 104
# The input tree is guaranteed to be a binary search tree.

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        res = ''

        def pre_order(root):
            nonlocal res
            if not root:
                res += 'None,'
                return
            res += (str(root.val) + ',')
            pre_order(root.left)
            pre_order(root.right)
        pre_order(root)
        return res

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        data = data.split(',')

        def dfs(data):
            if not data:
                return
            current = data.pop(0)
            root = TreeNode()
            if current == 'None':
                root = None
                return
            root.val = current
            root.left = dfs(data)
            root.right = dfs(data)
            return root

        return dfs(data)
