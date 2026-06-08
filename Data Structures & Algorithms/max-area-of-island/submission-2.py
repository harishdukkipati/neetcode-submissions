class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        visited = set()
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0 or (r,c) in visited:
                return 0 
            
            visited.add((r, c))
            return 1 + dfs(r, c-1) + dfs(r, c+1) + dfs(r+1, c) + dfs(r-1,c)
        
        for i in range(rows):
            for j in range(cols):
                if (i, j) not in visited and grid[i][j] == 1:
                    max_area = max(max_area, dfs(i, j))
        
        return max_area