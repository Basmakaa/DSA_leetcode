class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Edge case: if the array is empty
        if not nums:
            return 0
        
        # Initialize max and min product so far, and result
        max_so_far = nums[0]
        min_so_far = nums[0]
        result = nums[0]
        
        # Iterate through the array starting from the second element
        for i in range(1, len(nums)):
            num = nums[i]
            
            # Temporary variables to store the current max and min
            temp_max = max(num, num * max_so_far, num * min_so_far)
            temp_min = min(num, num * max_so_far, num * min_so_far)
            
            # Update max_so_far and min_so_far
            max_so_far = temp_max
            min_so_far = temp_min
            
            # Update result with the maximum product found so far
            result = max(result, max_so_far)
        
        return result
