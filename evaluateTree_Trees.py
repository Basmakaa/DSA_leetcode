# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def evaluateTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        #Intuition DFS Postoder as we want to process the children before the parent 
        #Approach 

        if not root :
            return None 
       
        self.evaluateTree(root.left)
        self.evaluateTree(root.right)

        if root.val == 2:
            root.val = root.left.val or root.right.val
        elif root.val == 3:
            root.val = root.left.val and root.right.val

        return root.val
        
