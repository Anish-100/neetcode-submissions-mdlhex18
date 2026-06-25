class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_num = -1
        row_length = len(matrix[0])-1
        # Find the row
        st, end = 0,len(matrix)-1
        while st <= end:
            middle = (end+st)//2
            if target >= matrix[middle][0] and target <= matrix[middle][row_length]:
                row_num = middle
                break
            elif target > matrix[middle][row_length]:
                st = middle +1 
            else:
                end = middle -1 
        if row_num == -1:
            return False
        row_matrix = matrix[row_num]
        st, end = 0,len(row_matrix)-1
        while st <= end:
            mid = (end+st)//2
            if row_matrix[mid] == target:
                return True
            elif target > row_matrix[mid]:
                st = mid +1 
            else:
                end = mid -1 
        return False