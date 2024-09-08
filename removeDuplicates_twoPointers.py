class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        #intuition : two pointers 
        #Approach : left pointers should start from L and move as long as there are duplicate, if we reach the third duplicate we move that duplicate to the end of the array 

        L= 0 
        R = 0 

        if len(nums)<=2:
            return len(nums)

        L=2

        for R in range(2, len(nums)):
            if nums[R] != nums[L-2]:
                nums[L] = nums[R]
                L+=1
        return L

        

            
        
