class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """

        #intuition dynamic programminf LCS
        #Approahc: see if any combination of s1 and s2 is a subsequence of s3
        N = len(s1)
        M = len(s2)
        K = len(s3)

        # Check if the lengths match
        if N + M != K:
            return False

        # DP table
        dp = [[False] * (M + 1) for _ in range(N + 1)]

        # Base case initialization
        dp[0][0] = True

        # Filling the first column (matching s1 with an empty s2)
        for i in range(1, N + 1):
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]

        # Filling the first row (matching s2 with an empty s1)
        for j in range(1, M + 1):
            dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]

        # Fill the rest of the dp table
        for i in range(1, N + 1):
            for j in range(1, M + 1):
                # Here we're using (i, j) but for strings, we use (i-1) and (j-1)
                dp[i][j] = (s1[i - 1] == s3[i + j - 1] and dp[i - 1][j]) or \
                           (s2[j - 1] == s3[i + j - 1] and dp[i][j - 1])

        return dp[N][M]
