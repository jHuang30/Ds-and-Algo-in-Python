# Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[20,9],[15,7]]
# Example 2:

# Input: root = [1]
# Output: [[1]]
# Example 3:

# Input: root = []
# Output: []
 

# Constraints:

# The number of nodes in the tree is in the range [0, 2000].
# -100 <= Node.val <= 100


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: 
            return []
        left_to_right = True
        next_level = []
        current_level = [root]
        res = []
        temp = []
        while current_level:
            current = current_level.pop()
            temp.append(current.val)
            if left_to_right:
                if current.left:
                    next_level.append(current.left)
                if current.right:
                    next_level.append(current.right)
            else:
                if current.right:
                    next_level.append(current.right)
                if current.left:
                    next_level.append(current.left)
            if not current_level:
                res.append(temp)
                temp = []
                current_level = next_level
                next_level = []
                left_to_right = not left_to_right
        return res


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue, res, left_to_right = [root], [], 1
        while queue:
            temp = []
            for i in range(len(queue)):
                current = queue.pop(0)
                temp.append(current.val)
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            res.append(temp[::left_to_right])
            left_to_right = -left_to_right
        return res