class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        rows,cols = len(matrix),len(matrix[0])
        l,r = 0, rows-1
        m  = 0
        while l<=r:
            mid = (r+l)//2
            if matrix[mid][0] <= target <= matrix[mid][cols-1]:
                m = mid
                break
            elif target < matrix[mid][0]:
                r= mid-1
            else:
                l = mid+1
        l,r = 0, cols-1
        while l<=r:
            mid = l + (r-l)//2
            if matrix[m][mid] == target:
                return True
            elif matrix[m][mid] > target:
                r= mid-1
            else:
                l = mid+1
        return False