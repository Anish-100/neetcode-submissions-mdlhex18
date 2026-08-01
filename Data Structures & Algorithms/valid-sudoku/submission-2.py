class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        column_visited = [set() for x in range(9)]
        squares_visited = [set() for x in range(9)]
        for i in range(len(board)):
            row_visited = set()
            for j in range(len(board[i])):
                if board[i][j] in row_visited or\
                 board[i][j] in column_visited[j] or \
                 board[i][j] in squares_visited[i//3 + ((j//3)*3)]:
                    return False
                if board[i][j] != '.':
                    row_visited.add(board[i][j])
                    column_visited[j].add(board[i][j])
                    squares_visited[i//3 + ((j//3)*3)].add(board[i][j])
        return True