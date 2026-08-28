class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        rows,cols = len(grid), len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]== 0:
                    q.append((i,j))  
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        level =1
        visited = set()
        while q:
            for _ in range(len(q)):
                i,j = q.popleft()
                for dr, dc in directions:
                    m,n = i+dr, j+dc
                    if m in range(rows) and n in range(cols):
                        if grid[m][n] != 0 and grid[m][n]!=-1 and (m,n) not in visited:
                            grid[m][n] = level
                            visited.add((m,n))
                            q.append((m,n))
            level+=1


            
