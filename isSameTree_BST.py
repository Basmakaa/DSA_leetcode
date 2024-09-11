class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

        def backtrack(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val :
                return False 
          
            return backtrack(p.left, q.left) and backtrack(p.right, q.right)
            
        
        return backtrack(p,q)
