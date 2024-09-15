# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.curr = root 
        self.stack = []


        

    def next(self):
        """
        :rtype: int
        """
        while self.curr:
            self.stack.append(self.curr)
            self.curr = self.curr.left
        res = self.stack.pop()
        self.curr = res.right
        return res.val

    def hasNext(self):
        """
        :rtype: bool
        """

        return bool(self.stack or self.curr)

