import math
import heapq
class Solution(object):

    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """

        max_heap = []

        for x,y in points :

            distance = -(x**2 + y**2)


            heapq.heappush(max_heap, (distance, [x,y]))

            if len(max_heap)> k :
                heapq.heappop(max_heap)
        
        return [point for _, point in max_heap]

        


