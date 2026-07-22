class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = set()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    islands.add((i,j))
        if not islands:
            return 0
        isCount = 0
        def dfs(i,j):
            if (i,j) not in islands:
                return None
            islands.remove((i,j))
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
            
        while islands:
           
            i,j = islands.pop()
            islands.add((i,j))
            dfs(i,j)
            isCount+=1
        return isCount
            
            



        