from collections import deque
class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        ROWS = len(grid)
        COLS = len(grid[0])
        queue = deque()
        visited = set()
        queue.append((0,0))
        visited.add((0,0))
        
        length = 0 
        if grid[0][0] == 1 or grid[ROWS-1][COLS-1] == 1:
            return -1

        while queue:
            for i in range(len(queue)):
                r,c = queue.popleft()
                if (r == ROWS-1 and c == COLS-1) :
                    return length +1
                
                neighboors = [[0,1], [0,-1], [1,0], [-1,0], [1,1], [-1,-1], [-1,1], [1,-1]]
                for dr,dc in neighboors:
                    if (min(dr+r,dc+c) <0 or dr+r == ROWS or dc+c == COLS or (dr+r,dc+c) in visited or grid[dr+r][dc+c] == 1) :
                        continue 
                
                    queue.append((dr+r,dc+c))
                    visited.add((dr+r,dc+c))

            length +=1
        return -1 
                



