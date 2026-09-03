class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        num_row = len(matrix)
        if num_row ==0:
            return False
        num_col = len(matrix[0])
        l = 0
        r = num_row * num_col

        while l<r:
            mid = (l+r)//2
            mid_row = mid // num_col
            mid_col = mid % num_col
            
            if mid_row > num_row-1 or mid_col > num_col -1:
                return False

            mid_val = matrix[mid_row][mid_col]

            if mid_val == target:
                return True
            elif mid_val <target:
                l = mid + 1
            else:
                r = mid
        
        return False