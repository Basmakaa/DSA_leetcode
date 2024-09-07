class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        #intuition use the skiding window 
        #Approach use a dictionary to keep the frequency of the character. Use sliding window to go over the string. keep track of the maximum frequency. and keep track that each window is valid or make it valid by shrinking the window until it becomes valid to make the maximum changes k 

        count = {}
        max_len = 0
        max_count = 0 
        L= 0
        for R in range(len(s)):
            count[s[R]] = count.get(s[R], 0) +1 
            max_count = max(max_count, count[s[R]])

            while (R-L+1) - max_count > k:
                count[s[L]] -= 1
                L+=1 

            max_len = max(max_len, R-L+1)

        return max_len 
        
        
