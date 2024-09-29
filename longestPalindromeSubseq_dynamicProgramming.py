class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [[0]* n for _ in range(n)]

        #base case every lette is a trivial palindrome 
        for i in range(n):
            dp[i][i] = 1

        for length in range(2, n+1):
            for l in range(n-length +1):
                r = l+ length -1 
                if s[l] == s[r]:
                    dp[l][r] = 2 + dp[l+1][r-1]
                else :
                    dp[l][r] = max( dp[l][r-1], dp[l+1][r])


        return dp[0][n-1]
    
