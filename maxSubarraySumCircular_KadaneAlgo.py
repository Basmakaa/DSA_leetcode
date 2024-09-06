class Solution(object):
    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        #Intuition: Kadane's algorithm 

        def kadane(nums):
            cursum = 0
            maxsum = nums[0]
            for n in nums: 
                if cursum < 0 :
                    cursum = 0
                cursum += n
                if cursum > maxsum :
                    maxsum = cursum
            return maxsum 

        normal_sum = kadane(nums)

        inverted = [-num for num in nums]
        min_sum = kadane(inverted)

        total = sum(nums)
        circular_sum = total + min_sum

        return max(circular_sum, normal_sum) if normal_sum > 0 else normal_sum
        
