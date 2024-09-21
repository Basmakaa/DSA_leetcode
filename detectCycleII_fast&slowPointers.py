# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #intuition: fast and slow pointers 

        #approach: reach when f = s, assign another slow pointers, keep on traversing until s1 =s2, this is the beginning of the cycle 
       
        f = head 
        s = head 
        
        while f and f.next :
            s = s.next
            f = f.next.next
            if f == s:
                break 
        if not f or not f.next :
            return None 

        s2 = head 

        while s != s2:
            s = s.next 
            s2 = s2.next 
        return s 
        
