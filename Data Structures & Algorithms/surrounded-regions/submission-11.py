class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        not_surrounded = set()
        def dfs(i,j, visited):
            if (i,j) in visited:
                return
            if i not in range(rows) or j not in range(cols):
                return
            visited.add((i,j))
            if board[i][j] == 'X':
                return
            if board[i][j] == 'O':
                not_surrounded.add((i,j))
            for dr, dc in directions:
                dfs(i+dr, j+dc, visited)
        for i in range(rows):
            for j in range(cols):
                if not (i == 0 or j == 0 or i == rows-1 or j == cols-1):
                    continue
                if board[i][j] == 'O':
                    not_surrounded.add((i,j))
                    dfs(i,j, set())
        for i in range(rows):
            for j in range(cols):
                if (i,j) in not_surrounded:
                    continue
                board[i][j] = 'X'