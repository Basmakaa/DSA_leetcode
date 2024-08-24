from collections import deque 
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue = deque()
        if root:
            queue.append(root)
        level = 0 
        result = []
        while len(queue) >0  :
            print(level)
            mylist = []
            for i in range(0, len(queue)):
                curr = queue.popleft()
                mylist.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            result.append(mylist)
            level+=1 
        return result 
