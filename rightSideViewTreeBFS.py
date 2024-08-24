from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        queue = deque()
        if root :
            queue.append(root)
        level = 0
        result = [] 
       
        while len(queue)>0:
            temp =[]
            for i in range(len(queue)):
                curr = queue.popleft()
                temp.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right: 
                    queue.append(curr.right)
            last_elem = temp[len(temp)-1]
            result.append(last_elem)
            level+=1
        return result 
