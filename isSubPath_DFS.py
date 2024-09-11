# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubPath(self, head, root):
        """
        :type head: ListNode
        :type root: TreeNode
        :rtype: bool
        """
        
        def check_root(head, root):
            if not head :
                return True 
            if not root:
                return False 
            if root.val != head.val:
                return False 

            return check_root(head.next, root.left) or check_root(head.next, root.right)
        def preorder(root):
            if not root:
                return False
            return check_root(head, root) or preorder(root.left) or preorder(root.right)

    
        return preorder(root)
