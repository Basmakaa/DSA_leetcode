class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        #Intuition :djisktra algo 
        src = (0,0)
        adj = {}

        for i in range(0, len(grid)):
            for j in range(0,len(grid)):
                 adj[(i,j)] = []
               
        for i in range(0, len(grid)):
            for j in range(0,len(grid)):
                
                if i > 0:  # Up
                    adj[(i, j)].append([(i - 1, j), grid[i - 1][j]])
                if i < len(grid) - 1:  # Down
                    adj[(i, j)].append([(i + 1, j), grid[i + 1][j]])
                if j > 0:  # Left
                    adj[(i, j)].append([(i, j - 1), grid[i][j - 1]])
                if j < len(grid) - 1:  # Right
                    adj[(i, j)].append([(i, j + 1), grid[i][j + 1]])

        shortest = {}
        minheap = [[grid[0][0], src]]
        mymax = grid[0][0] 
        while minheap :
            w1, n1 = heapq.heappop(minheap)
            if n1 in shortest :
                continue 
            shortest[n1] = w1
            mymax = max(mymax, w1)
            # If we reach the bottom-right corner, return the max elevation
            if n1 == (len(grid) - 1, len(grid) - 1):
                return mymax

            for n2, w2 in adj[n1] :
                if n2 not in shortest :
                    heapq.heappush(minheap, [max(w1,w2), n2])

        return -1
        
