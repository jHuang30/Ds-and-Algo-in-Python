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
            if current == 'None':
                return None
            root = TreeNode(current)
            root.left = dfs(data)
            root.right = dfs(data)
            return root

        return dfs(data)



# using min and max to determin if it's the leaf of the tree

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        res = []

        def pre_order(root):
            if not root:
                return
            res.append(str(root.val))
            pre_order(root.left)
            pre_order(root.right)

        pre_order(root)
        return ' '.join(res)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        vals = [int(i) for i in data.split()]

        def dfs(min_val, max_val):
            if vals and (min_val < vals[0] < max_val):
                current = vals.pop(0)
                root = TreeNode(current)
                root.left = dfs(min_val, current)
                root.right = dfs(current, max_val)
                return root

        return dfs(float('-inf'), float('inf'))
