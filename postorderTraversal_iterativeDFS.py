class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        
        stack = [root]
        visited= [False]
        res = []

        while stack :
            curr = stack.pop()
            vis = visited.pop()
            if curr:

                if vis :
                    res.append(curr.val)

                

                else:
                    stack.append(curr)
                    visited.append(True)
                    stack.append(curr.right)
                    visited.append(False)
                    stack.append(curr.left)
                    visited.append(False)
        return res
