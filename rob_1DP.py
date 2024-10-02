class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #intuition : DP
        #Approach use 1D DP table where dp[i] hold the max mount of money than can be robbed up to house i 
        if not nums :
            return 0
        if len(nums) ==1 :
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        dp = [0] * (len(nums)+1)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], nums[i]+ dp[i-2])

        return dp[len(nums)-1]
        
