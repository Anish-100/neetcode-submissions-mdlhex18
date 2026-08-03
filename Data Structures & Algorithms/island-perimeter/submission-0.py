class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        total_sum = 0
        rows,cols = len(grid), len(grid[0])
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    running_sum = 4
                    for dr, dc in directions:
                        if i+dr in range(rows) and j+dc in range(cols):
                            if grid[i+dr][j+dc] == 1:
                                running_sum-=1
                    total_sum+=running_sum
        return total_sum


        