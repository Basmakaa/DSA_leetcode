from collections import deque

class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ROWS = len(grid)
        COLS = len(grid[0])
        queue = deque()
        visit = set()
        fresh_count = 0
        
        # Enqueue all initially rotten oranges and count fresh oranges
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r, c))
                    visit.add((r, c))
                elif grid[r][c] == 1:
                    fresh_count += 1
        
        # If there are no fresh oranges, return 0 (all oranges are rotten)
        if fresh_count == 0:
            return 0
        
        # Directions for BFS
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        length = 0
        
        # Perform BFS
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in visit and grid[nr][nc] == 1:
                        grid[nr][nc] = 2  # Rotten the orange
                        fresh_count -= 1
                        queue.append((nr, nc))
                        visit.add((nr, nc))
            
            length += 1
        
        # If there are still fresh oranges left, return -1
        return length - 1 if fresh_count == 0 else -1
