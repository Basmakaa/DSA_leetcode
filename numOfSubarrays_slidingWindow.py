class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        #intuition : using a sliding window of length k 
        #Approach : use sliding window of k, calculate average everytime we move the sliding window 

        L= 0
        R = 0 
        av = 0 
        res = 0
        target_sum = k * threshold 
        for i in range(k):
            av += arr[i]
        if av >= target_sum :
            res+=1
        for R in range(k, len(arr)) :
            av += arr[R]
            av -= arr[L]
            L+=1
            if av >= target_sum :
                res +=1 
            R+=1 
            
        return res
