class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col_map = {}
        block_data = {}
        for i in range(len(board)):
            row_map = set()
            for j in range(len(board[i])):
                if j not in col_map:
                    col_map[j] = set()
                if board[i][j] == '.':
                    continue
                # deal with 3x3
                block_code = (int(i/3),int(j/3))
                if block_code not in block_data:
                    print(block_code)
                    block_data[block_code] = set()
                if board[i][j] in block_data[block_code]:
                    print('3x3 False',block_data)
                    return False
                else:
                    block_data[block_code].add(board[i][j])
                # deal with row issue
                if board[i][j] in row_map:
                    print(board[i][j])
                    print('row False',row_map)
                    return False
                else:
                    row_map.add(board[i][j])

                # deal with column issue:
                if board[i][j] in col_map[j]:
                    print('col False')
                    return False
                else:
                    col_map[j].add(board[i][j])

        return True
        
        