class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        countMap = {}
        for i in range(0,len(nums)):
            if nums[i] not in countMap:
                countMap[nums[i]] = 1
            else:
                return True 
        return False 
