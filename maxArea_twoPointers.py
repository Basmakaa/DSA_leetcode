class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        #Intuition : 2 pointers L andd R
        #approach : Area = Length x Width = (x2 - x1) x min(height1, height2). go over the height array using pointer R, and up
        R=len(height) -1 
        L=0
        max_water = 0 
        while R != L:
            
            area = (R- L)* min(height[L], height[R])
            if area > max_water:
                max_water = area 

            if height[L] < height[R]:
                L+=1
            else:
                R-=1
        return max_water
