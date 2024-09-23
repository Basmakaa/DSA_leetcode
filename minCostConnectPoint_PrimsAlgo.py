import heapq

class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points)
        
        # Helper function to calculate Manhattan distance between two points
        def manhattan_distance(p1, p2):
            return abs(points[p1][0] - points[p2][0]) + abs(points[p1][1] - points[p2][1])

        # Prim's Algorithm to find the Minimum Spanning Tree (MST)
        
        # Min-heap stores (cost, point_index) starting with the first point
        minheap = [(0, 0)]  # Starting with point 0 with cost 0
        visit = set()  # Set to track visited points
        total_cost = 0  # To accumulate the total cost
        
        while len(visit) < n:
            # Extract the point with the minimum cost
            weight, point = heapq.heappop(minheap)
            
            # If this point is already visited, skip it
            if point in visit:
                continue
            
            # Add point to the MST
            visit.add(point)
            total_cost += weight
            
            # Explore neighbors (other points)
            for neighbor in range(n):
                if neighbor not in visit:
                    # Calculate the Manhattan distance to the neighbor
                    dist = manhattan_distance(point, neighbor)
                    heapq.heappush(minheap, (dist, neighbor))

        return total_cost
