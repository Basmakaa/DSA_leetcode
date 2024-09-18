class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pivot = 0
        total_sum = 0 
        pivot_sum = 0
        for i in range(0,len(nums)):
            total_sum += nums[i]
        for i in range(0,len(nums)):
            pivot_sum += nums[i]
            if i ==0 and total_sum - pivot_sum == 0 :
                return 0 
            if pivot_sum - nums[i] == total_sum - pivot_sum :
                return i 
        return -1
