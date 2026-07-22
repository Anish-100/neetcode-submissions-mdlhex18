# dfs solution
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        rows,cols = len(grid), len(grid[0])
        def dfs(m,n): 
            if m not in range(rows) or n not in range(cols) or grid[m][n] == 0:
                return 0
            grid[m][n] = 0
            return 1 + dfs(m+1,n)+ dfs(m-1,n)+ dfs(m,n+1)+ dfs(m,n-1)
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    max_area = max(max_area, dfs(i,j))
        return max_area
