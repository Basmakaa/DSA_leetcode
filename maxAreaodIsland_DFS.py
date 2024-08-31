class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def dfs(r, c, visit):
            ROWS = len(grid)
            COLS = len(grid[0])
            
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in visit or grid[r][c] == 0:
                return 0
            
            visit.add((r, c))
            count = 1  # Start with the current cell
            count += dfs(r + 1, c, visit)  # Down
            count += dfs(r - 1, c, visit)  # Up
            count += dfs(r, c + 1, visit)  # Right
            count += dfs(r, c - 1, visit)  # Left
            
            return count
        
        visit = set()
        max_area = 0
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r, c) not in visit and grid[r][c] == 1:
                    area = dfs(r, c, visit)
                    max_area = max(max_area, area)
        
        return max_area
