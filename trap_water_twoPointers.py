class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0

        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        unit = 0

        while left < right:
            if left_max < right_max:
                left+=1
                left_max = max(left_max, height[left])
                unit += left_max  - height[left]
                
            else:
                right -=1
                right_max = max(right_max, height[right])
                unit += right_max - height[right]
                

        return unit
        
