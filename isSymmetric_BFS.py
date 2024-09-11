from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        queue = deque()
        result = []

        if root:
            queue.append(root)

        while queue:
            for i in range(len(queue)):
                curr = queue.popleft()
                if curr is None :
                    result.append(1000)
                
                else:
                    result.append(curr.val)
                    queue.append(curr.left)
                    queue.append(curr.right)
            
            if result != result[::-1] :
                return False
            result = []
        return True 
