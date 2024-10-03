class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        word_set = set(wordDict)  # Convert to set for O(1) lookups
        dp = [False] * (len(s) + 1)  # DP array to store if s[0:i] can be segmented
        dp[0] = True  # Empty string can always be segmented
        
        # Iterate over the entire string
        for i in range(1, len(s) + 1):
            # Check all possible breaks
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break  # No need to check further if dp[i] is True
        
        return dp[len(s)]  # The result is whether the whole string can be segmented
