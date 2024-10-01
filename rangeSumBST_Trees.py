# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.mysum = 0
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        #intuition preorder, go over all the tree and sum up the elements betweeen high and low inclusive, use a global variable for that
        def helper(root):
            if not root:
                return 
            if low <= root.val <= high :
                self.mysum += root.val
            if root.val > low:
                helper(root.left)
            if root.val <high :
                helper(root.right)

        helper(root)

        return self.mysum

