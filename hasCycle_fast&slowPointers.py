# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        #Intuition : Fast and Slow pointers 
        #Approach : Go over the linked list using two pointers f and s where f is faster than s two times. If F and S intersect then it means that there is a cycle else return False
        f = head 
        s = head 
        if head == None :
            return False 

        while f and f.next :
            s = s.next 
            f = f.next.next
            if f == s :
                return True 
        return False 
        
