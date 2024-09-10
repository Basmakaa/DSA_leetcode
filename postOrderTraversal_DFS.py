# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        result = []
        def backtrack(root, result):
            if not root:
                return 
            backtrack(root.left,result)
            backtrack(root.right, result )
            result.append(root.val)

        backtrack(root, result)
        return result 
        
