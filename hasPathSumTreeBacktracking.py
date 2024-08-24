# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum, path) :
        if not root :
            return False 
        path.append(root.val)
        if not root.left and not root.right  :
            if sum(path) == targetSum :
                return True
            
        if self.pathSum(root.left,targetSum, path) :
            return True 
        if self.pathSum(root.right,targetSum,path) :
            return True 
        path.pop()
        return False 

    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        return self.pathSum(root, targetSum, [])

        
