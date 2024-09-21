# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        #intuition : fast and slow pointers 
        #approach, find the middle, reverse second half, addition element i of first hald with element i of second hald, then keep on updating max sum 
        f = head 
        s = head 
        res = 0

        while f and f.next:
            s = s.next 
            f = f.next.next 
        mid = s 
        prev = None 
        while s :
            next_node = s.next 
            s.next = prev 
            prev = s
            s = next_node

        
        s = head 
        f = prev 
        res = 0 

        while f :
            sm = s.val + f.val
            res = max(res, sm)
            f = f.next 
            s = s.next

        return res 

        
