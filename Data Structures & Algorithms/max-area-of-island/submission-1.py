
from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        cArea = 0
        rows,cols = len(grid), len(grid[0])
        def bfs(m,n):
            nonlocal cArea
            q = deque()
            q.append((m,n))
            while q:
                i,j = q.popleft()
                directions = [[-1,0],[1,0],[0,-1],[0,1],[0,0]]
                for dr, dc in directions:
                    m,n = i + dr, j+dc
                    if m in range(rows) and n in range(cols) and grid[m][n] == 1:
                        cArea+=1
                        q.append((m,n))
                        grid[m][n] = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    bfs(i,j)
                    max_area = max(cArea, max_area)
                    cArea = 0
        return max_area


        