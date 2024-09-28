class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """

        #intuition : dynamic programming 
        #Approach : determine if each day is a travel day or not, if not travel day the cost remaint the same, if it is, get the min cost of 3 scenarios of passes. Update the dp table each time 

        last_day =days[-1]
        dp = [0]* (last_day+1)
        days_set = set(days)

        for d in range(1, last_day+1): 
            if d not in days_set:
                dp[d] = dp[d-1]
            else:
                scenario1 = dp[d-1] + costs[0]
                scenario2 = dp[max(0,d-7)] + costs[1]
                scenario3 = dp[max(0, d-30)] + costs[2]
                dp[d] = min(scenario1, scenario2, scenario3)

        return dp[last_day]




