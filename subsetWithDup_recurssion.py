class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #intuition: recurssion 

        #Approach 

        # Sort the list 
        # use a helper method to do the recurssion, for eahc path we choose if we include each specific or we include at least one time that element 

        curr = []
        res = []
        nums.sort()

        def helper(i) :
            if i >= len(nums):
                res.append(list(curr))
                return

            #include element 
            curr.append(nums[i])
            helper(i+1)
            curr.pop()
            #doesn't include element, skip all duplicates
            while (i <len(nums)-1 and nums[i] == nums[i+1]) :
                i+=1 
            helper(i+1)

    
        helper(0)
        return res

    
