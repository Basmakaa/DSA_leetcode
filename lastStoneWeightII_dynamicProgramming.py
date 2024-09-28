class Solution(object):
    def lastStoneWeightII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        #intiuition dynamic programming, we're lookinf for the minimal sum based on the order of adding or sbstracting eachh element 
        #Approach : for each number we wither add it or remove it 
        # Total sum of all stones
        total = sum(stones)
        
        # Target is to find a subset as close as possible to total // 2
        target = total // 2
        
        # DP array: dp[i] will be True if a subset with sum i is possible
        dp = [False] * (target + 1)
        dp[0] = True  # A subset with sum 0 is always possible (the empty subset)
        
        # Process each stone
        for stone in stones:
            # Update the dp array in reverse to avoid using the same stone twice
            for i in range(target, stone - 1, -1):
                dp[i] = dp[i] or dp[i - stone]
        
        # Find the maximum possible subset sum that is less than or equal to target
        for i in range(target, -1, -1):
            if dp[i]:
                # The answer is total - 2 * i
                return total - 2 * i

            
