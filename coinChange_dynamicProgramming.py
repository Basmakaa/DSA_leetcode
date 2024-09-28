class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        #intuition: dynamic programming problem, 
        #Approach use a dp table where the result is the minimum number coins used for a certain amount 
        dp = [float('inf')] * (amount+1)
        dp[0] = 0

        for coin in coins:
            for x in range(coin, amount+1):
                dp[x] = min(dp[x], dp[x-coin]+1)
        
        return dp[amount] if dp[amount] != float('inf') else -1
