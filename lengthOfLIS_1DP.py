class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp= [1] *(len(nums)+1)
        
        
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i] >nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)

        return max(dp)
