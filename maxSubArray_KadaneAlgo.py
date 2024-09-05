class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cursum = 0
        maxsum = nums[0]

        for n in nums :
            if cursum <0:
                cursum = 0
            cursum += n 
            if cursum >maxsum :
                maxsum = cursum

        return maxsum

