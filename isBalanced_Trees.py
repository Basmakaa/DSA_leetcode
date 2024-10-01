# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self,root):
        def height(node):
            if not node:
                return 0
            
            left_height = height(node.left)
            right_height = height(node.right)
            
            # Condition 1: If any subtree is unbalanced, propagate -1 upwards
            if left_height == -1 or right_height == -1:
                return -1
            
            # Condition 2: If the current node is unbalanced, return -1
            if abs(left_height - right_height) > 1:
                return -1
            
            # Return height of current node
            return 1 + max(left_height, right_height)
        
        return height(root) != -1
