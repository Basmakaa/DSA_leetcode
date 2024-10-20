# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getLonelyNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """

        #intuition : DFS preorder traversal 
        #approach : check each time if parent have 2 children 

        result =[]

        def dfs(root):
            if not root :
                return 

            if not root.left and root.right :
                result.append(root.right.val)
            if root.left and not root.right :
                result.append(root.left.val)
            
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return result 

