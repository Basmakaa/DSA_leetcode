class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """

        #intuition : dynamic programming
        #approach : 

        N = len(text1)
        M = len(text2)
        dp = [[0]*(M+1) for _ in range(N+1)]

        for i in range(N):
            for j in range(M):
                if text1[i] == text2[j]:
                    dp[i+1][j+1] = 1 + dp[i][j]
                else :
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
        

        return dp[N][M]
        
