# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.diameter = 0

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def helper(root):
            if not root :
                return 0
            
            left = helper(root.left)
            right = helper(root.right)
            self.diameter = max(self.diameter, left + right)

            return 1 + max(left, right)
            

        helper(root)
        return self.diameter

        
