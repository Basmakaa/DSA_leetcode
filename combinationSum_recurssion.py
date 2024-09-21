class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        #intuition : recurssion 

        curr = []
        res= []
        def helper(i):
            if sum(curr) == target :
                res.append(list(curr))
                return 
            if sum(curr) >target:
                return

            for j in range(i, len(candidates)):
                curr.append(candidates[j])
                helper(j)
                curr.pop()

        helper(0)
        return res

        
