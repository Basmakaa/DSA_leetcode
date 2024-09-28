class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        N = len(word1)
        M = len(word2)
        dp = [[0]*(M+1) for _ in range(N+1)]
        
        #base cases:
        for i in range(N+1):
            dp[i][0] = i # delete all characters 
        for j in range(M+1):
            dp[0][j] = j #add all character 

        for i in range(N):
            for j in range(M):
                if word1[i] == word2[j]:
                    dp[i+1][j+1] = dp[i][j]
                else:
                    dp[i+1][j+1] = 1+ min(dp[i+1][j], dp[i][j+1], dp[i][j])
                
        return dp[N][M]

        
