class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        #intuition : 1D dp
        #approach : dp[i] is the numbe of ways to decode the string up till string at i 
        # Edge case: If the string is empty or starts with '0', it's invalid
        if not s or s[0] == '0':
            return 0
        
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1  # There's one way to decode an empty string
        
        # A single character can be decoded if it's not '0'
        dp[1] = 1 if s[0] != '0' else 0
        
        for i in range(2, n + 1):
            # Check if single digit decode is valid
            if 1 <= int(s[i-1:i]) <= 9:
                dp[i] += dp[i-1]
            
            # Check if two digit decode is valid
            if 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]
        
        return dp[n]
