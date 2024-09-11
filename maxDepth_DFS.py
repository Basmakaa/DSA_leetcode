class Solution(object):
    def __init__(self):
        self.max_value = 0

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def traversal(root, count) :
            if not root:
                self.max_value = max(self.max_value, count)
                return 
            traversal(root.left, count +1)
            traversal(root.right, count +1)

        traversal(root,0)

        return self.max_value
