class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # recursion 
        #approach :  use a helper method, and either include or not include each element 
        res = []
        curr = []
        def helper(i, nums,curr,res) :
            #base case, end of path 
            if i >= len(nums) :
                res.append(list(curr))
                return

            #include element 
            curr.append(nums[i])
            helper(i+1, nums, curr, res)
            curr.pop()

            helper(i+1, nums, curr, res)

            

        helper(0, nums, curr, res)
        return res


    
