# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def __init__(self):
        self.closest = None
    def closestValue(self, root, target):
        """
        :type root: Optional[TreeNode]
        :type target: float
        :rtype: int
        """
        # Initialize the closest value with root's value
        self.closest = root.val
        def dfs(node):
            if not node:
                return

            # Update closest if the current node is closer to the target
            if abs(target - node.val) < abs(target - self.closest) or \
               (abs(target - node.val) == abs(target - self.closest) and node.val < self.closest):
                self.closest = node.val

            # Continue DFS
            if target > node.val:
                dfs(node.right)
            elif target < node.val:
                dfs(node.left)
        
        # Start DFS traversal from the root
        dfs(root)

        return self.closest
