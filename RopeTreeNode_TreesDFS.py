# Definition for a rope tree node.
# class RopeTreeNode(object):
#     def __init__(self, len=0, val="", left=None, right=None):
#         self.len = len
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getKthCharacter(self, root, k):
        """
        :type root: Optional[RopeTreeNode]
        :type k: int
        :rtype: str
        """

        #intuition : dfs traversal until we get to leaf and store string 
        #Approach L 
        result = []
        def dfs(root):
            if not root:
                return 
            if not root.left and not root.right :
                for char in root.val:
                    result.append(char)
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        return result[k-1] if len(result)>= k else  None
        
