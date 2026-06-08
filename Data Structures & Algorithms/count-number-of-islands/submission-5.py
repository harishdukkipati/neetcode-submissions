#Understand 
# island is formed if the 1's are all connected 

#Plan 
# keep a track of the amount of islands 
# let rows = len(gird) and cols = len(grid[0])
# visited set
# create a dfs function that takes in row index and cols index
# check if it's out of bounds or in visited set 
# return 
# dfs in all 4 directions 

# iterate through grid check if row, col in grid
# only if it is in it then do dfs and increment count by 1

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        count = 0
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or (r, c) in visited or grid[r][c] == "0":
                return 
            
            visited.add((r, c))
            dfs(r, c+1)
            dfs(r, c-1)
            dfs(r+1, c)
            dfs(r-1, c)

        for i in range(rows):
            for j in range(cols):
                if (i, j) not in visited and grid[i][j] == "1":
                    dfs(i, j)
                    count += 1
        
        return count