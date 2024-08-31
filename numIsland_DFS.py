class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def dfs(grid, r, c, visit):
            ROWS = len(grid)
            COLS = len(grid[0])
            
            # Check boundaries and if the cell is water or already visited
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or (r, c) in visit or grid[r][c] == '0':
                return 0
            
            # Mark the cell as visited
            visit.add((r, c))
            
            # Traverse all 4 directions
            dfs(grid, r-1, c, visit)  # Up
            dfs(grid, r+1, c, visit)  # Down
            dfs(grid, r, c-1, visit)  # Left
            dfs(grid, r, c+1, visit)  # Right
            
            return 1
        
        if not grid or not grid[0]:
            return 0
        
        visit = set()
        count = 0
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r, c) not in visit and grid[r][c] == '1':
                    count += dfs(grid, r, c, visit)
        
        return count
