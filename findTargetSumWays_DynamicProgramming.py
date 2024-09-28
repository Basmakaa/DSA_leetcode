class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        #Intuition Dynamic programming, using memoization 
        #Approach each element add or substract it and return 1 if sum = target or 0 if not

        memo ={ }

        def findWays(i,total) :
            if i == len(nums) :
                return 1 if target == total else 0 
            if (i,total) in memo:
                return memo[(i,total)]
            
            add = findWays(i+1, nums[i] + total)
            substract = findWays(i+1, total - nums[i])

            memo[(i,total)] = add + substract 

            return memo[(i,total)]


        return findWays(0,0)

        
