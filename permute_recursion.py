class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def helper(i,nums):
            #base case: if we're out of bound
            if i == len(nums):
                return [[]]
            
            res = []
            curr = helper(i+1, nums)
            for p in curr:
                for j in range(len(p)+1):
                    pcopy = list(p)
                    pcopy.insert(j, nums[i])
                    res.append(pcopy)
            return res 

        return helper(0,nums)

        
        
