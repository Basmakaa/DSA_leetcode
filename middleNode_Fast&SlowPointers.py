class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = head
        slow = head 

        while fast and fast.next :
            slow = slow.next 
            fast = fast.next.next
        return slow 
        
