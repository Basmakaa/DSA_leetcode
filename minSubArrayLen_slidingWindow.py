class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        L = 0 
        R = 0 
        res =0
        length = float("inf")
        for R in range(len(nums)):
            res += nums[R]
            while res >= target:
                length = min(length, R-L+1)
                res -= nums[L]
                L+=1

            R+=1 
        return 0 if length == float("inf") else length 

        
