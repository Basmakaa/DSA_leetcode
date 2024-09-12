class Solution(object):
    def __init__(self):
        self.min_value = float('inf')
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #intuition : DFS 
        #Approach : use DFS 
        if not root:
            return 0
    
        def traversal(root, count):
            if not root.left and not root.right:
                self.min_value = min(self.min_value, count)
                return 
            if root.left:
                traversal(root.left, count+1)
            if root.right:
                traversal(root.right, count+1)
        traversal(root, 1)

        return self.min_value




