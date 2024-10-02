class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        #intuition : dynamic programming 
        #Approach : have a 1D dp table dp[i] holds the minimum cost to reach step i 
        dp= [0] * (len(cost)+1)
        dp[0] = 0 
        dp[1]= 0
        
        for i in range(2,len(cost)+1):
            dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2]) 

        return dp[len(cost)]
