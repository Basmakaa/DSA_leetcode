class Solution(object):
    def maxTurbulenceSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        if len(arr) == 1:
            return 1
        
        max_len = 1
        start = 0
        
        for i in range(1, len(arr)):
            c = (arr[i] > arr[i-1]) - (arr[i] < arr[i-1])
            
            if c == 0:
                start = i
            elif i == 1 or c * ((arr[i-1] > arr[i-2]) - (arr[i-1] < arr[i-2])) != -1:
                start = i - 1
            
            max_len = max(max_len, i - start + 1)
        
        return max_len
