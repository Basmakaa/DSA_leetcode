# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        def isequal(root,subRoot):
            if not root and not subRoot:
                return True
            if not root or not subRoot:
                return False
            if root.val != subRoot.val :
                return False 
            
            return isequal(root.left, subRoot.left) and isequal(root.right, subRoot.right)
            
        def preorder(root):
            if not root:
                return None 
            if root.val == subRoot.val and isequal(root,subRoot):
                return True
            
            return preorder(root.left) or preorder(root.right)
        return preorder(root)

        
