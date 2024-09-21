class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = nums[0]
        f = nums[0]

        while True:
            s = nums[s]
            f = nums[nums[f]]
            if s == f:
                break 
        
        s2 = nums[0]
        while s2 != s:
            s = nums[s]
            s2 = nums[s2]
        return s

        
