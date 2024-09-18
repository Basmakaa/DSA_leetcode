class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.prefix = []
        total = 0
        for n in nums :
            total += n 
            self.prefix.append(total) 
        

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        preRight = self.prefix[right]
        preLeft = self.prefix[left-1] if left >0 else 0
        return preRight - preLeft 
        
