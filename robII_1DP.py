class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Intuition DP as we can solve that into subproblems 
        # Approach : add 2 pointers 
        if len(nums) == 0:
            return 0 
        if len(nums) == 1:
            return nums[0]
        def helper(houses):
            n = len(houses)
            if n == 0:
                return 0
            if n == 1:
                return houses[0]
            
            # DP array to store the max amount up to each house
            dp = [0] * n
            dp[0] = houses[0]
            dp[1] = max(houses[0], houses[1])
            
            for i in range(2, n):
                dp[i] = max(dp[i-1], houses[i] + dp[i-2])
            
            return dp[-1]

        return max(helper(nums[:-1]), helper(nums[1:]))
