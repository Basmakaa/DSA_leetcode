class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #intuition dynamic programming
        #Approach : if the sum is odd we can't find equal subset sum, if its even, then we need to find a subset that is equal to half of the total sum fo the array 
        if sum(nums) %2 == 1:
            return False


        target = sum(nums) //2 
        dp = [False] * (target +1) 
        dp[0]= True

        for n in nums:
            for s in range(target, n-1,-1) :
                if dp[s-n] :
                    dp[s]= True
        return dp[target]

