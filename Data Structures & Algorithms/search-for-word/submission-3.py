class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        self.res = False
        path = []
        len_p, len_w = len(path), len(word)
        rows,cols = len(board),len(board[0])
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        def backtrack(i,j, curr,visited):
            if i not in range(rows) or j not in range(cols) or curr >= len_w:
                return
            if ''.join(path) == word:
                self.res = True
                return
            if curr > -1 and path[curr] != word[curr]:
                return
            if len_p >=len_w:
                return
            visited.add((i,j))
            for dr, dc in directions:
                m,n = i+dr, j+dc
                if (m,n) not in visited:
                    path.append(board[i][j])
                    if ''.join(path) == word:
                        self.res = True
                        return
                    visited.add((m,n))
                    backtrack(m,n, curr+1,visited)
                    visited.remove((m,n))
                    path.pop()
        for i in range(rows):
            for j in range(cols):
                backtrack(i,j,-1,set())
        return self.res